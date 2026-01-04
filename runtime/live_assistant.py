import sys
import time
import threading
from typing import Optional

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread, pyqtSignal, QObject, QTimer

from overlay.overlay_window import OverlayWindow
from overlay.geometry import HearthstoneGeometry, Point
from runtime.log_watcher import LogWatcher
from runtime.parser import LogParser
from ai.game_state import GameState
from simulator.game import Game
from simulator.player import Player
from simulator.enums import Zone

class AssistantWorker(QThread):
    """Background worker that watches logs and updates the AI state."""
    
    # Signals to update GUI safely
    status_signal = pyqtSignal(str)   # Main action text
    info_signal = pyqtSignal(str)     # Details/Confidence text
    winrate_signal = pyqtSignal(float) # Value estimate -1 to 1
    arrow_signal = pyqtSignal(object, object)
    highlight_signal = pyqtSignal(object)
    
    def __init__(self, use_model: bool = True):
        super().__init__()
        self.running = True
        self.game = Game()
        self.parser = LogParser(self.game)
        self.watcher = LogWatcher(self.handle_log_line)
        self.geometry = HearthstoneGeometry()
        
        # AI Brain (AlphaZero model)
        self.use_model = use_model
        self.brain = None
        if use_model:
            try:
                from ai.brain import AIBrain
                self.brain = AIBrain()
                if self.brain.load_latest_model():
                    print("AlphaZero model loaded successfully!")
                else:
                    print("No trained model found. Using dummy AI.")
                    self.brain = None
            except Exception as e:
                print(f"Failed to load AI Brain: {e}")
                self.brain = None
        
        # Initialize basic players for parser context
        p1 = Player("Player 1", self.game)
        p2 = Player("Player 2", self.game)
        self.game.players = [p1, p2]
        self.game.current_player_idx = 0
        
    def run(self):
        """Main loop in thread."""
        self.status_signal.emit("Searching...")
        self.info_signal.emit("Hearthstone logs scanner active")
        
        # The watcher.start() is blocking, so run it in a separate thread
        self.watcher_thread = threading.Thread(target=self.watcher.start, daemon=True)
        self.watcher_thread.start()
        
        while self.running:
            # Periodically refresh suggestions if nothing happened in logs
            # (In case something changed but didn't trigger a log line right away)
            self._refresh_suggestions()
            time.sleep(1)

    def stop(self):
        """Signals the thread and its children to stop."""
        self.running = False
        self.watcher.stop()
    
    def _refresh_suggestions(self):
        """Periodically refresh suggestions based on current game state."""
        # Find player with cards
        me = None
        for p in self.game.players:
            if p.hand or p.board:
                me = p
                break
        
        if me:
            self.think_and_suggest()
        
    def handle_log_line(self, line: str):
        """Called for every new log line."""
        # 1. Parse
        self.parser.parse_line(line)
        
        # 2. Check for Turn Decision
        current_p = self.game.current_player
        # Assuming P1 is "Me" (Local Player). 
        # In real parser we need to distinct "Friendly" from "Opposing".
        # For now assume P1 (Index 0) is us.
        
        if self.game.current_player_idx == 0: 
            # It's our turn!
            self.think_and_suggest()
        else:
            self.status_signal.emit("Opponent's Turn")
            self.arrow_signal.emit(None, None) # Clear arrows

    def think_and_suggest(self):
        """AI Logic - Uses AlphaZero model if available, fallback to dummy AI."""
        # Check if Hearthstone is running and a game is active
        if not self.game or not self.game.players:
            self.status_signal.emit("STANDBY")
            self.info_signal.emit("Waiting for game...")
            return

        # Perspective 1 for local player
        state = GameState.from_simulator_game(self.game, perspective=1)
        
        # === USE ALPHAZERO MODEL IF AVAILABLE ===
        if self.brain is not None:
            self._suggest_with_brain(state)
            return

        # === DUMMY AI FALLBACK ===
        self.status_signal.emit("DUMMY AI")
        me = self.game.players[0]
        
        # === PRIORITY 1: Playable Cards ===
        playable = [c for c in me.hand if hasattr(c, 'cost') and c.cost <= me.mana]
        
        if playable:
            card_to_play = playable[0]
            card_name = getattr(card_to_play.data, 'name', card_to_play.card_id)
            
            self.status_signal.emit(f"PLAY: {card_name}")
            self.info_signal.emit(f"Dummy AI suggests playing {card_name}")
            
            hand_size = len(me.hand)
            card_index = me.hand.index(card_to_play)
            card_pos = self.geometry.get_hand_card_pos(card_index, hand_size)
            self.highlight_signal.emit(card_pos)
            return
        
        self.status_signal.emit("NO ACTIONS")
        self.info_signal.emit("No playable pieces.")

    def _suggest_with_brain(self, state: GameState):
        """Use AlphaZero model for suggestions."""
        from ai.actions import ActionType
        
        # Get suggestion from brain
        action, confidence, description = self.brain.suggest_action(state)
        
        if action is None:
            self.status_signal.emit("IDLE")
            self.info_signal.emit(description)
            return
        
        # Display confidence and description
        conf_pct = int(confidence * 100)
        self.status_signal.emit(description.upper())
        self.info_signal.emit(f"AI Strategy | Confidence: {conf_pct}%")
        
        # Get value estimate (winrate)
        value = self.brain.get_value_estimate(state)
        self.winrate_signal.emit(value)
        
        # Visualize the action
        me = self.game.players[0]
        
        if action.action_type == ActionType.END_TURN:
            self.arrow_signal.emit(None, None)
            
        elif action.action_type == ActionType.PLAY_CARD:
            if action.card_index is not None and action.card_index < len(me.hand):
                hand_size = len(me.hand)
                card_pos = self.geometry.get_hand_card_pos(action.card_index, hand_size)
                self.highlight_signal.emit(card_pos)
                
        elif action.action_type == ActionType.HERO_POWER:
            hp_pos = self.geometry.get_hero_power_pos(is_opponent=False)
            self.highlight_signal.emit(hp_pos)
            
        elif action.action_type == ActionType.ATTACK:
            if action.attacker_index is not None and action.target_index is not None:
                # Attacker position
                if action.attacker_index < len(me.board):
                    start_pos = self.geometry.get_player_minion_pos(action.attacker_index, len(me.board))
                    # Target position
                    if action.target_index == -1:  # Face
                        end_pos = self.geometry.get_hero_pos(is_opponent=True)
                    else:
                        # Enemy minion
                        enemy = self.game.players[1]
                        if action.target_index < len(enemy.board):
                            end_pos = self.geometry.get_opponent_minion_pos(action.target_index, len(enemy.board))
                        else:
                            end_pos = self.geometry.get_hero_pos(is_opponent=True)
                    self.arrow_signal.emit(start_pos, end_pos)

    def _suggest_attacks(self, me):
        """Suggest creature attacks after card plays."""
        if not me.board:
            return  # No minions to attack with
        
        # Find opponent
        opponent = None
        for p in self.game.players:
            if p != me:
                opponent = p
                break
        
        if not opponent:
            return
        
        # Check for Taunt minions on opponent's board
        taunt_minions = [m for m in opponent.board if hasattr(m, 'taunt') and m.taunt]
        
        # Get first attacker (simplified: assume all can attack)
        attacker = me.board[0]
        attacker_index = 0
        
        if taunt_minions:
            # Must attack taunt
            target = taunt_minions[0]
            target_index = opponent.board.index(target)
            target_pos = self.geometry.get_opponent_minion_pos(target_index, len(opponent.board))
        else:
            # Go face!
            target_pos = self.geometry.get_hero_pos(is_opponent=True)
        
        attacker_pos = self.geometry.get_player_minion_pos(attacker_index, len(me.board))
        
        # Debug
        print(f"[DEBUG] Board size: {len(me.board)}, Attacker index: {attacker_index}")
        print(f"[DEBUG] Attacker pos: ({attacker_pos.x}, {attacker_pos.y})")
        print(f"[DEBUG] Target pos: ({target_pos.x}, {target_pos.y})")
        
        # Get attacker name
        attacker_name = attacker.data.name if hasattr(attacker, 'data') and attacker.data else "Minion"
        
        if taunt_minions:
            target_name = target.data.name if hasattr(target, 'data') and target.data else "Taunt"
            self.status_signal.emit(f"Attack: {attacker_name} → {target_name}")
        else:
            self.status_signal.emit(f"Attack: {attacker_name} → Face")
        
        self.arrow_signal.emit(attacker_pos, target_pos)

def main():
    app = QApplication(sys.argv)
    
    # 1. Get screen resolution
    screen = QApplication.primaryScreen()
    if screen:
        screen_geo = screen.geometry()
        screen_width = screen_geo.width()
        screen_height = screen_geo.height()
    else:
        screen_width = 1920
        screen_height = 1080
    
    # 2. Overlay
    window = OverlayWindow()
    window.show()
    
    # 3. Worker Thread
    worker = AssistantWorker()
    worker.geometry.resize(screen_width, screen_height)  # IMPORTANT: Use real screen resolution
    worker.status_signal.connect(window.update_info)
    worker.arrow_signal.connect(window.set_arrow)
    worker.highlight_signal.connect(window.set_highlight)
    worker.start()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
