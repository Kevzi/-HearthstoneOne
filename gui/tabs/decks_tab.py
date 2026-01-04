from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
    QScrollArea, QFrame, QApplication, QGridLayout
)
from PyQt6.QtGui import QColor, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt, QSize
import sys

from simulator.deck_generator import DeckGenerator
from simulator.card_loader import CardDatabase

class ManaCurveWidget(QWidget):
    def __init__(self, card_costs):
        super().__init__()
        self.setFixedHeight(60)
        self.costs = card_costs # dict {cost: count}
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        if not self.costs:
            return
            
        max_count = max(self.costs.values()) if self.costs else 1
        width = self.width()
        height = self.height()
        
        bar_width = width / 8 # 0-7+
        gap = 4
        
        painter.setBrush(QBrush(QColor("#3b82f6"))) # Blue
        painter.setPen(Qt.PenStyle.NoPen)
        
        for cost in range(8):
            count = 0
            if cost == 7:
                for c, n in self.costs.items():
                    if c >= 7: count += n
            else:
                count = self.costs.get(cost, 0)
                
            if count > 0:
                bar_height = (count / max_count) * (height - 10)
                x = cost * bar_width + gap/2
                y = height - bar_height
                painter.drawRoundedRect(int(x), int(y), int(bar_width - gap), int(bar_height), 2, 2)
                
                # Draw count text
                painter.setPen(QColor("white"))
                painter.drawText(int(x), int(y - 2), int(bar_width - gap), 10, Qt.AlignmentFlag.AlignCenter, str(count))
                painter.setBrush(QBrush(QColor("#3b82f6")))
                painter.setPen(Qt.PenStyle.NoPen)

class DeckCardItem(QFrame):
    def __init__(self, class_name, deck_name, deck_code, parent_tab):
        super().__init__()
        self.parent_tab = parent_tab
        self.code = deck_code
        self.deck_name = deck_name
        self.class_name = class_name
        
        self.setProperty("class", "deck-item")
        self.setStyleSheet("""
            QFrame[class="deck-item"] {
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 8px;
            }
            QFrame[class="deck-item"]:hover {
                border: 1px solid #3b82f6;
                background-color: #334155;
            }
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedHeight(80)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        
        # Icon / Class Color Strip
        strip = QFrame()
        strip.setFixedWidth(4)
        strip.setStyleSheet(f"background-color: {self.get_class_color(class_name)}; border-radius: 2px;")
        layout.addWidget(strip)
        
        # Text Info
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        
        name_lbl = QLabel(deck_name)
        name_lbl.setStyleSheet("font-weight: bold; font-size: 14px; color: white;")
        
        class_lbl = QLabel(class_name.upper())
        class_lbl.setStyleSheet("font-size: 10px; color: #94a3b8; font-weight: bold; letter-spacing: 1px;")
        
        text_layout.addWidget(name_lbl)
        text_layout.addWidget(class_lbl)
        layout.addLayout(text_layout)
        
        layout.addStretch()
        
        # Arrow
        arrow = QLabel("→")
        arrow.setStyleSheet("color: #64748b; font-size: 18px;")
        layout.addWidget(arrow)

    def mousePressEvent(self, event):
        self.parent_tab.load_deck_details(self.deck_name, self.class_name, self.code)

    def get_class_color(self, cls):
        colors = {
            "Death Knight": "#1f2937",
            "Demon Hunter": "#10b981",
            "Druid": "#fb923c",
            "Hunter": "#4ade80",
            "Mage": "#3b82f6",
            "Paladin": "#facc15",
            "Priest": "#e2e8f0",
            "Rogue": "#94a3b8",
            "Shaman": "#2563eb",
            "Warlock": "#a855f7",
            "Warrior": "#ef4444"
        }
        return colors.get(cls, "#64748b")

class DecksTab(QWidget):
    def __init__(self):
        super().__init__()
        self.db = CardDatabase.get_instance()
        if not self.db._loaded: self.db.load()
        self.init_ui()
        
    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        
        # 1. Left Panel: Deck List (Scrollable)
        left_container = QWidget()
        left_layout = QVBoxLayout(left_container)
        left_layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Meta Decks Library")
        title.setStyleSheet("font-size: 20px; font-weight: 800; color: white; margin-bottom: 10px;")
        left_layout.addWidget(title)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        self.deck_list_widget = QWidget()
        self.deck_list_layout = QVBoxLayout(self.deck_list_widget)
        self.deck_list_layout.setSpacing(10)
        self.deck_list_layout.addStretch() # Push items up
        
        scroll.setWidget(self.deck_list_widget)
        left_layout.addWidget(scroll)
        
        refresh_btn = QPushButton("Refresh Database")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #334155; color: white; border: none; 
                padding: 10px; border-radius: 6px; font-weight: bold;
            }
            QPushButton:hover { background-color: #475569; }
        """)
        refresh_btn.clicked.connect(self.load_decks)
        left_layout.addWidget(refresh_btn)
        
        main_layout.addWidget(left_container, 4) # 40% width
        
        # Divider
        div = QFrame()
        div.setFixedWidth(1)
        div.setStyleSheet("background-color: #334155;")
        main_layout.addWidget(div)
        
        # 2. Right Panel: Deck Details
        self.right_panel = QWidget()
        self.right_panel.setVisible(False) # Hidden by default
        right_layout = QVBoxLayout(self.right_panel)
        right_layout.setContentsMargins(30, 30, 30, 30)
        right_layout.setSpacing(15)
        
        # Detail Header
        self.detail_name = QLabel("Deck Name")
        self.detail_name.setStyleSheet("font-size: 24px; font-weight: 800; color: white;")
        self.detail_class = QLabel("CLASS")
        self.detail_class.setStyleSheet("font-size: 12px; font-weight: bold; color: #94a3b8; letter-spacing: 1px;")
        
        right_layout.addWidget(self.detail_name)
        right_layout.addWidget(self.detail_class)
        
        # Mana Curve Placeholder
        self.curve_container = QWidget()
        self.curve_layout = QVBoxLayout(self.curve_container)
        self.curve_layout.setContentsMargins(0,0,0,0)
        right_layout.addWidget(QLabel("Mana Curve"))
        right_layout.addWidget(self.curve_container)
        
        # Card List Area
        self.card_scroll = QScrollArea()
        self.card_scroll.setWidgetResizable(True)
        self.card_scroll.setStyleSheet("border: none; background: transparent;")
        
        self.card_list_widget = QWidget()
        self.card_list_layout = QVBoxLayout(self.card_list_widget)
        self.card_list_layout.setSpacing(2)
        self.card_list_layout.addStretch()
        
        self.card_scroll.setWidget(self.card_list_widget)
        right_layout.addWidget(self.card_scroll)
        
        # Copy Button
        self.copy_btn = QPushButton("Copy Deck Code")
        self.copy_btn.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6; color: white; border: none;
                padding: 12px; border-radius: 6px; font-weight: bold;
            }
            QPushButton:hover { background-color: #2563eb; }
        """)
        self.copy_btn.clicked.connect(self.copy_current_code)
        right_layout.addWidget(self.copy_btn)
        
        main_layout.addWidget(self.right_panel, 6) # 60% width
        
        # Placeholder for right panel when empty
        self.empty_state = QLabel("Select a deck to view details")
        self.empty_state.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_state.setStyleSheet("color: #64748b; font-size: 16px;")
        main_layout.addWidget(self.empty_state, 6)
        
        self.load_decks()
        
    def load_decks(self):
        # Clear existing
        while self.deck_list_layout.count() > 1: # Keep stretch
            item = self.deck_list_layout.itemAt(0)
            if item.widget(): item.widget().deleteLater()
            self.deck_list_layout.removeItem(item)
            
        try:
            decks = DeckGenerator._load_meta_decks()
            # Sort by Class then Name
            decks.sort(key=lambda x: (x[0], x[1]))
            
            for class_name, deck_name, deck_code in decks:
                item = DeckCardItem(class_name, deck_name, deck_code, self)
                self.deck_list_layout.insertWidget(self.deck_list_layout.count()-1, item)
                
        except Exception as e:
            print(f"Error loading decks: {e}")

    def load_deck_details(self, name, cls, code):
        self.current_code = code
        self.empty_state.setVisible(False)
        self.right_panel.setVisible(True)
        
        self.detail_name.setText(name)
        self.detail_class.setText(cls.upper())
        
        # Clear list
        while self.card_list_layout.count() > 1:
            item = self.card_list_layout.itemAt(0)
            if item.widget(): item.widget().deleteLater()
            self.card_list_layout.removeItem(item)
            
        # Clear curve
        if self.curve_layout.count() > 0:
            item = self.curve_layout.itemAt(0)
            if item.widget(): item.widget().deleteLater()
            self.curve_layout.removeItem(item)

        # Parse Code and Sideboards
        cards = []
        sideboards = {}
        try:
            if isinstance(code, list):
                card_ids = code
            else:
                decoded = DeckGenerator.decode_deck_string(code)
                if isinstance(decoded, dict):
                    card_ids = decoded.get("cards", [])
                    sideboards = decoded.get("sideboards", {})
                else:
                    card_ids = decoded or []
        except:
            card_ids = []
            
        # Count & Stats (Main Deck)
        counts = {}
        costs = {}
        for cid in card_ids:
            counts[cid] = counts.get(cid, 0) + 1
            
        card_objs = []
        for cid, qty in counts.items():
            c = self.db.get_card(cid)
            if c:
                card_objs.append({'card': c, 'qty': qty, 'type': 'MAIN'})
                costs[c.cost] = costs.get(c.cost, 0) + qty
        
        # Add Sideboards
        for parent, children in sideboards.items():
            for cid in children:
                c = self.db.get_card(cid)
                if c:
                    card_objs.append({'card': c, 'qty': 1, 'type': 'SIDE'})

        # Draw Curve (Main Deck Only)
        self.curve_layout.addWidget(ManaCurveWidget(costs))
        
        # Sort by Cost (Main then Side)
        card_objs.sort(key=lambda x: (0 if x['type']=='MAIN' else 1, x['card'].cost))
        
        for item in card_objs:
            card = item['card']
            qty = item['qty']
            is_side = item['type'] == 'SIDE'
            
            row = QFrame()
            row.setFixedHeight(30)
            rl = QHBoxLayout(row)
            rl.setContentsMargins(5, 0, 5, 0)
            
            # Badge Cost
            cost_badge = QLabel(str(card.cost))
            cost_badge.setFixedSize(20, 20)
            cost_badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
            bg_col = "#3b82f6" if not is_side else "#64748b" # Gray for side
            cost_badge.setStyleSheet(f"background-color: {bg_col}; color: white; border-radius: 3px; font-weight: bold;")
            rl.addWidget(cost_badge)
            
            # Name
            name_text = card.name
            if is_side: name_text = f"↳ {name_text}"
            
            name_lbl = QLabel(name_text)
            color = "#e2e8f0"
            if card.rarity == 3: color = "#60a5fa" 
            if card.rarity == 4: color = "#a855f7" 
            if card.rarity == 5: color = "#facc15" 
            if is_side: color = "#94a3b8" # Override color for side to dim it slightly
            
            font_style = "italic" if is_side else "normal"
            name_lbl.setStyleSheet(f"color: {color}; font-size: 13px; font-style: {font_style};")
            rl.addWidget(name_lbl)
            
            rl.addStretch()
            
            # Qty
            qty_str = f"x{qty}"
            if card.rarity == 5 and not is_side: qty_str = "★"
            
            qty_lbl = QLabel(qty_str)
            qty_lbl.setStyleSheet("color: #64748b; font-weight: bold;")
            rl.addWidget(qty_lbl)
            
            self.card_list_layout.insertWidget(self.card_list_layout.count()-1, row)
            
    def copy_current_code(self):
        if hasattr(self, 'current_code') and isinstance(self.current_code, str):
            QApplication.clipboard().setText(self.current_code)
            self.copy_btn.setText("Copied to Clipboard!")
            QTimer.singleShot(2000, lambda: self.copy_btn.setText("Copy Deck Code"))
            
