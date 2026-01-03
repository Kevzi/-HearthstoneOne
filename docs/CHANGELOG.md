# 📜 Changelog

Toutes les modifications notables du projet HearthstoneOne.

---

## [2026-01-03] — Live Assistant & Overlay

### ✨ Ajouté
- **`runtime/live_assistant.py`** — Orchestrateur complet combinant Parser + Overlay + IA (dummy)
- **`overlay/overlay_window.py`** — Fenêtre transparente PyQt6 avec dessin de flèches et cercles
- **`overlay/geometry.py`** — Calcul des positions écran (main, board, héros)
- **`runtime/parser.py`** — Support FULL_ENTITY + format réel Hearthstone
- Extraction de `zonePos` depuis les logs
- Suggestions d'attaque (créature → cible)
- Détection des Taunt adverses
- Cercles dorés pour les cartes sans cible

### 🔧 Modifié
- **`runtime/log_watcher.py`** — Auto-reconnexion si lancé avant Hearthstone
- **`runtime/parser.py`** — Parsing robuste avec regex flexibles
- **`simulator/player.py`** — Ajout de `setaside` et `choices`
- **`simulator/factory.py`** — Correction assignation contrôleur

### 📚 Documenté
- `README.md` entièrement réécrit avec diagrammes Mermaid
- `docs/TASKS.md` mis à jour avec toutes les phases

---

## [2026-01-02] — Training Pipeline

### ✨ Ajouté
- **`training/trainer.py`** — Boucle d'entraînement PyTorch
- **`training/data_collector.py`** — Collecte de trajectoires via self-play
- **`ai/replay_buffer.py`** — Stockage optimisé des données

### 🧪 Testé
- Proof of Life : Loss qui descend après quelques itérations

---

## [2026-01-01] — Core AI

### ✨ Ajouté
- **`ai/model.py`** — Réseau Actor-Critic (Policy + Value heads)
- **`ai/mcts.py`** — Monte Carlo Tree Search avec UCB
- **`ai/encoder.py`** — Encodage état de jeu en tenseur (690 dimensions)
- **`evaluation.py`** — Script d'évaluation basique

---

## [2025-12-31] — Simulateur Universel

### ✨ Ajouté
- **`simulator/game.py`** — Moteur de jeu complet
- **`simulator/player.py`** — Gestion joueur (main, board, deck)
- **`simulator/entities.py`** — Cartes, Serviteurs, Héros, Pouvoirs
- **`simulator/card_loader.py`** — Chargement depuis hearthstone_data
- **`simulator/enums.py`** — Énumérations (Zone, CardType, etc.)

### 🔧 Modifié
- Migration complète depuis Fireplace vers simulateur custom

---

## [2025-12-30] — Setup Initial

### ✨ Ajouté
- Structure du projet
- `requirements.txt`
- Architecture de base
