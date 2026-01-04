# 📜 Changelog

All notable changes to the HearthstoneOne project.

---

## [2026-01-04] — Hub Redesign & MCTS Performance
- **Unity Hub Aesthetic** — Complete GUI overhaul following the "DeepMana Hub" design (Dark theme, Blue accents, Rounded elements).
- **MCTS Optimization (3x Speedup)** — Reusing internal simulator objects and caching Action metadata to drastically reduce computational overhead.
- **Improved Live Assistant** — Stable communication between the overlay and background threads using signals and real `GameState` objects.
- **Bug Fixes** — Resolved multiple missing imports (PyQt6) and corrected AI suggestion logic in SpyTab.

---

## [2026-01-04] — Simulator Mechanics V1.1 (Tradeable, Forge, Magnetic)

### ✨ Added
- **Tradeable Logic** — AI can now trade cards (1 mana) to shuffle them into the deck and draw a replacement.
- **Forge Logic** — Added support for upgrading cards in hand (2 mana).
- **Expanded Targeting** — Redesigned the AI action space (300 indices) to support full targeting of friendly minions.
- **Magnetic Support** — AI can now choose specific friendly Mechs to fuse with when playing Magnetic minions.

### 🔧 Changed
- **Graveyard Order** — Deaths are now resolved strictly by `summon_timestamp`, ensuring correct deathrattle sequences.
- **Action space** — Increased `PLAY_CARD` target resolution from 10 to 20 slots per card (300 indices total).
- **Extended Game Limits** — Increased maximum steps per game from 150/200 to **500** to allow for long matches.

### 🧪 Fixed
- **Missing Actions** — Enabled `TRADE` and `FORGE` actions in the `HearthstoneGame` wrapper for training.
- **Resolved excessive draws** — Refactored `MCTS` simulation to use centralized `wrapper.step()`, allowing the AI to correctly evaluate attacks and effects in its "thinking" phase.
- **GUI Compactness** — Optimized Dashboard layout by reducing margins (60px → 30px), window dimensions (1100x850 → 980x720), and element scales (Logo 240px → 160px) for a more efficient interface.
- **Action Index Offset Symmetry** — Fixed a bug where `CHOOSE`, `TRADE`, and `FORGE` indices overlapped with `PLAY_CARD` targets.

---

## [2026-01-04] — Fairness & Turbo Performance

### ✨ Added
- **Turbo Configuration** — Added support for `training_config.json` to optimize workers (up to 15) and MCTS simulations for high-end CPUs (AMD Ryzen 5800X).
- **Persistent Analytics** — Training statistics (Loss, Winrate, Buffer) are now saved to `training_history.json`, ensuring dashboard data survives restarts.
- **Plot Enhancements** — Added markers to analytics graphs for visibility even with a single data point.
- **Reset Utility** — Created `tools/reset_training.py` to quickly clear models and history for fresh starts.

### 🔧 Changed
- **Balanced Self-Play** — Random perspective assignment in `data_collector.py` (AI can be P1 or P2) and confirmed "The Coin" (`GAME_005`) logic for P2.
- **Effect Package Scoping** — Fixed `EffectCache` to correctly set `__package__`, allowing relative imports within card effects.

### 🧪 Fixed
- **Double Draw Bug** — Resolved issue where players drew 2 cards instead of 1 at the start of their turn.
- **Multiprocessing NameErrors** — Fixed worker crashes caused by undefined `hero1`/`hero2` in `reset()` and missing `encoder` instance.
- **Maze Guide Import** — Fixed `ModuleNotFoundError` in `REV_308` by removing invalid `simulator.rng` dependency and streamlining the effect.
- **CSS Lints** — Corrected multiple syntax and property errors in `gui/style.css`.

---

## [2026-01-03] — Training Pipeline Stability & Sideboard Fix

### ✨ Added
- **Dual Deck Format** — `meta_decks.json` now supports both `"code"` (deckstrings) and `"cards"` (direct ID lists).
- **Starcraft Card Effects** — Implemented SC_759 (Shield Battery), SC_760 (Resonance Coil), SC_764 (Sentry), SC_783 (Void Ray).
- **Additional Effects** — TIME_432 (Intertwined Fate), TLC_100 (Elise the Navigator), CORE_AV_329 (Thrive in the Shadows).

### 🔧 Changed
- **`simulator/deck_generator.py`** — Refactored `_load_meta_decks()` to return list format with dual format support.
- **`gui/tabs/decks_tab.py`** — Updated to handle both deckstring and direct card list formats.
- **Sideboard Filter** — Added intelligent filtering to ignore corrupted sideboard entries (count > 2, dbfId < 100).

### 🧪 Fixed
- **Multiprocessing Crash** — Resolved `QObject: Cannot create children for a parent in different thread` by isolating stdout redirection.
- **Sideboard Parsing Bug** — Fixed Zilliax/E.T.C. deck codes that caused `too many values to unpack` errors.
- **Protoss Priest Deck** — Corrected card IDs (CORE_AV_329 → CS3_028) and added all 30 cards manually.
- **Wisp Fallback** — Added safety fallback with WARNING logs for unknown card IDs.

---

## [2026-01-03] — Meta Decks JSON & Starcraft Support

### ✨ Added
- **`data/meta_decks.json`** — Externalized deck definitions for easier management.
- **Starcraft Custom Set** — Implemented effects for Photon Cannon, Artanis, Mothership.
- **Custom User Decks** — Added support for user-provided "New Priest" and "New Warlock" archetypes.
- **Data Improver** — `CardDatabase` now prioritizes `data/cards.json` and applies patches from `data/manual_cards.json` to fix missing 2026 cards.

### 🔧 Changed
- **`simulator/deck_generator.py`** — Major refactor to load decks from JSON files dynamically.
- **`gui/tabs/decks_tab.py`** — Updated to consume the new JSON-based deck generator.
- **Model Reset** — Purged old checkpoints to allow fresh training on the fully corrected dataset.

### 🧪 Fixed
- **"Unknown Card" Bug** — Resolved issues with missing DBF IDs by utilizing `manual_cards.json` patches and verifying against HSGuru codes.

---

## [2026-01-03] — Dashboard v1.0 & Fixes

### ✨ Added
- **Dashboard GUI** — Complete training control center with Real-time Stats (Winrate, Loss).
- **Meta Decks Library** — GUI tab to browse 120+ top-tier decks with "View List" popup.
- **Deck Decoder** — Integrated logic to decode DeckStrings into readable card lists (Name, Mana, Count).
- **Stop Button** — Safe training interruption mechanism in `trainer.py`.

### 🔧 Fixed
- **Nozdormu Crash** — Implemented native `dormant` mechanic to prevent simulated crashes.
- **Dynamic Cloning** — Fixed `entities.py` to recursively copy custom attributes (preventing future crashes).
- **Empty Deck List** — Added error handling and visual feedback when decoding decks.
- **Localization** — Full translation of the Interface and Documentation to **English**.

---

## [2026-01-03] — High-Speed Training & Premium Overlay

### ✨ Added
- **Multiprocessing Support** — `training/data_collector.py` now uses 8 parallel workers.
- **Premium Overlay** — New Glassmorphism design with neon effects and pulsating animations.
- **Win Probability** — Dynamic display of win probability (AI Value Head).
- **TensorBoard** — Live tracking of training metrics (Loss, Winners, Buffer).
- **Meta Decks Support** — Integration of 120+ meta decks (HSGuru January 2026).
- **Auto-Validator** — `tools/verify_effects.py` to validate 1800+ effect scripts.
- **Resume System** — Automatic saving and loading of checkpoints (weights + optimizer).

### 🔧 Changed
- **`training/data_collector.py`** — Complete refactor for parallelism.
- **`runtime/live_assistant.py`** — Full AlphaZero AI integration for suggestions.
- **`overlay/overlay_window.py`** — Major aesthetic improvements.
- **Card Fixes** — Massive validation of trigger signatures (on_turn_end, etc.).

---

## [2026-01-03] — Live Assistant & Overlay (V1)

### 🔧 Changed
- **`runtime/log_watcher.py`** — Auto-reconnection if launched before Hearthstone.
- **`runtime/parser.py`** — Robust parsing with flexible regex.
- **`simulator/player.py`** — Added `setaside` and `choices`.
- **`simulator/factory.py`** — Fixed controller assignment.

### 📚 Documented
- `README.md` completely rewritten with Mermaid diagrams.
- `docs/TASKS.md` updated with all phases.

---

## [2026-01-02] — Training Pipeline

### ✨ Added
- **`training/trainer.py`** — PyTorch Training Loop.
- **`training/data_collector.py`** — Trajectory collection via self-play.
- **`ai/replay_buffer.py`** — Optimized data storage.

### 🧪 Tested
- Proof of Life: Decreasing Loss after a few iterations.

---

## [2026-01-01] — Core AI

### ✨ Added
- **`ai/model.py`** — Actor-Critic Network (Policy + Value heads).
- **`ai/mcts.py`** — Monte Carlo Tree Search with UCB.
- **`ai/encoder.py`** — Game state encoding to tensor (690 dimensions).
- **`evaluation.py`** — Basic evaluation script.

---

## [2025-12-31] — Universal Simulator

### ✨ Added
- **`simulator/game.py`** — Complete Game Engine.
- **`simulator/player.py`** — Player management (hand, board, deck).
- **`simulator/entities.py`** — Cards, Minions, Heroes, Powers.
- **`simulator/card_loader.py`** — Loading from hearthstone_data.
- **`simulator/enums.py`** — Enumerations (Zone, CardType, etc.).

### 🔧 Changed
- Complete migration from Fireplace to custom simulator.

---

## [2025-12-30] — Initial Setup

### ✨ Added
- Project structure.
- `requirements.txt`.
- Base architecture.
