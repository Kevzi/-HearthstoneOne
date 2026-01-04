# 📚 Documentation HearthstoneOne

Bienvenue dans la documentation technique du projet.

---

## 📁 Contenu

| Fichier | Description |
|---------|-------------|
| [TASKS.md](TASKS.md) | Feuille de route et suivi des tâches |
| [CHANGELOG.md](CHANGELOG.md) | Historique des modifications |
| [PHASE0_UNIVERSAL_SIMULATOR.md](PHASE0_UNIVERSAL_SIMULATOR.md) | Architecture du simulateur |
| [SIMULATOR_ANALYSIS.md](SIMULATOR_ANALYSIS.md) | Analyse comparative des simulateurs |

---

## 🏗️ Architecture Globale

```
HearthstoneOne
├── ai/                # Intelligence Artificielle
├── simulator/         # Moteur de jeu
├── runtime/           # Interface temps réel
├── overlay/           # Interface graphique
├── training/          # Entraînement IA
└── docs/              # Documentation (vous êtes ici)
```

---

## 🔗 Liens Utiles

- **Repository** : [GitHub](https://github.com/Kevzi/-HearthstoneOne)
- **Données Cartes** : [hearthstone_data](https://github.com/HearthSim/python-hearthstone)

---

## 📖 Guides

### Lancer l'Assistant

```bash
cd HearthstoneOne
python runtime/live_assistant.py
```

### Entraîner l'IA

```bash
python training/trainer.py
```

### Évaluer le Modèle

```bash
python evaluation.py
```

---

## ⚠️ Status & Known Limitations (v1.2)

| Feature | Status | Notes |
|---------|--------|-------|
| Graveyard Order | ✅ | Deaths resolved in summon order. |
| Complex Triggers | ⚠️ | "Whenever" vs "After" timing might be slightly off in nested chains. |
| Magnetic | ✅ | Full support for targeting Mechs. |
| Tradeable | ✅ | Fully implemented (1 mana draw cycle). |
| Forge | ✅ | Fully implemented (2 mana upgrade logic). |
| Hand Targeting | ✅ | Friendly targeting enabled in Action Space (300 indices). |
| Draw Resolution | ✅ | MCTS now correctly evaluates attacks and effects. |
| GUI Density | ✅ | Compact Dashboard layout (980x720). |
