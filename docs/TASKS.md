# 📋 HearthstoneOne — Feuille de Route

> Dernière mise à jour : 2026-01-03

---

## ✅ Phase 0: Simulateur Universel

| Tâche | Statut |
|-------|--------|
| Architecture du simulateur | ✅ |
| Moteur de jeu de base | ✅ |
| Système de triggers et événements | ✅ |
| Génération d'effets via LLM | ✅ |
| Trackers d'historique | ✅ |
| Validation cartes complexes (Rembobinage) | ✅ |
| Wrapper RL | ✅ |

---

## ✅ Phase 1: Structures de Données

| Tâche | Statut |
|-------|--------|
| `game_wrapper.py` | ✅ |
| `game_state.py` | ✅ |
| `actions.py` | ✅ |
| Tests unitaires | ✅ |

---

## ✅ Phase 2: Self-Play Engine

| Tâche | Statut |
|-------|--------|
| `self_play.py` | ✅ |
| Tests self-play | ✅ |

---

## ✅ Phase 3: Core AI (MCTS + Neural Network)

| Tâche | Statut |
|-------|--------|
| `model.py` — Réseau Actor-Critic | ✅ |
| `encoder.py` — Encodage état/actions | ✅ |
| `mcts.py` — Monte Carlo Tree Search | ✅ |
| Game State Cloning | ✅ |
| Tests AI core | ✅ |

---

## ✅ Phase 4: Training Loop

| Tâche | Statut |
|-------|--------|
| `replay_buffer.py` — Stockage trajectoires | ✅ |
| `data_collector.py` — Self-play parallèle | ✅ |
| `trainer.py` — Boucle PyTorch | ✅ |
| Proof of Life (Loss qui descend) | ✅ |

---

## 🚧 Phase 5: Évaluation & Optimisation

| Tâche | Statut |
|-------|--------|
| Script `evaluation.py` | ✅ |
| Optimisation MCTS | ⏳ |
| Hyperparameter Tuning | ⏳ |

---

## ⏳ Phase 6: Interface Graphique (GUI)

| Tâche | Statut |
|-------|--------|
| `gui/main_window.py` | ⏳ |
| Dashboard stats | ⏳ |
| Visualisation Replay Buffer | ⏳ |

---

## ✅ Phase 7: Runtime (Logs & Parser)

| Tâche | Statut |
|-------|--------|
| `runtime/log_watcher.py` — Surveillance Power.log | ✅ |
| Auto-reconnexion (polling) | ✅ |
| `runtime/parser.py` — Parsing TAG_CHANGE | ✅ |
| `runtime/parser.py` — Parsing FULL_ENTITY | ✅ |
| Extraction ZONE, DAMAGE, CONTROLLER | ✅ |
| Extraction zonePos | ✅ |
| Gestion SETASIDE (Discover) | ✅ |
| Tests parser | ✅ |

---

## ✅ Phase 8: Overlay Graphique

| Tâche | Statut |
|-------|--------|
| `overlay/overlay_window.py` — Fenêtre transparente | ✅ |
| `overlay/geometry.py` — Calcul positions écran | ✅ |
| Flèches vertes (cartes ciblées) | ✅ |
| Cercles dorés (cartes sans cible) | ✅ |
| `runtime/live_assistant.py` — Orchestrateur | ✅ |
| Suggestions de cartes | ✅ |
| Suggestions d'attaques | ✅ |
| Détection Taunt | ✅ |
| Filtre par mana | ✅ |

---

## ⏳ Phase 9: Fonctionnalités Avancées

| Tâche | Statut |
|-------|--------|
| Pouvoir Héroïque (suggestion + overlay) | ⏳ |
| Lieux / Locations | ⏳ |
| Multi-flèches (plusieurs suggestions) | ⏳ |
| Parsing mana (tag RESOURCES) | ⏳ |
| Calibrage géométrie écran | ⏳ |

---

## ⏳ Phase 10: Intégration IA Entraînée

| Tâche | Statut |
|-------|--------|
| Connecter `model.py` à `live_assistant.py` | ⏳ |
| MCTS en temps réel (inférence) | ⏳ |
| Export ONNX | ⏳ |
| Inférence GPU optimisée | ⏳ |

---

## 📊 Résumé

| Phase | Statut |
|-------|--------|
| Phase 0 — Simulateur | ✅ Terminée |
| Phase 1 — Structures | ✅ Terminée |
| Phase 2 — Self-Play | ✅ Terminée |
| Phase 3 — Core AI | ✅ Terminée |
| Phase 4 — Training | ✅ Terminée |
| Phase 5 — Évaluation | 🚧 En cours |
| Phase 6 — GUI | ⏳ À venir |
| Phase 7 — Runtime | ✅ Terminée |
| Phase 8 — Overlay | ✅ Terminée |
| Phase 9 — Avancé | ⏳ À venir |
| Phase 10 — Intégration | ⏳ À venir |
