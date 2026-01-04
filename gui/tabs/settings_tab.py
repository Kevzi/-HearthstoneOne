from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame, 
                             QLabel, QSpinBox, QComboBox, QPushButton, QFormLayout)
import json
import os

CONFIG_FILE = "training_config.json"

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(20)
        
        # Title
        title = QLabel("System Configuration")
        title.setStyleSheet("font-size: 24px; font-weight: 800; color: #f8fafc;")
        self.layout.addWidget(title)
        
        # Config Card
        card = QFrame()
        card.setProperty("class", "card")
        form_layout = QFormLayout(card)
        form_layout.setSpacing(20)
        form_layout.setLabelAlignment(__import__("PyQt6.QtCore").QtCore.Qt.AlignmentFlag.AlignLeft)
        
        # 1. Hardware Settings
        self.spin_workers = QSpinBox()
        self.spin_workers.setRange(0, 32)
        self.spin_workers.setValue(8)
        self.spin_workers.setSuffix(" cores")
        
        self.combo_device = QComboBox()
        self.combo_device.addItems(["Auto (CUDA if available)", "Force CPU", "Force CUDA"])
        
        form_layout.addRow(self.create_label("CPU Workers", "Parallel processes for self-play"), self.spin_workers)
        form_layout.addRow(self.create_label("Compute Device", "Hardware accelerator for training"), self.combo_device)
        
        # 2. Training Hyperparameters
        self.spin_batch = QSpinBox()
        self.spin_batch.setRange(16, 512)
        self.spin_batch.setValue(64)
        self.spin_batch.setSingleStep(16)
        
        self.spin_mcts = QSpinBox()
        self.spin_mcts.setRange(10, 800)
        self.spin_mcts.setValue(25)
        
        form_layout.addRow(self.create_label("Batch Size", "Samples per gradient update"), self.spin_batch)
        form_layout.addRow(self.create_label("MCTS Simulations", "Thinking steps per move"), self.spin_mcts)
        
        self.layout.addWidget(card)
        
        # Save Button
        self.btn_save = QPushButton("Save Configuration")
        self.btn_save.setObjectName("start_btn") # Re-use green button style
        self.btn_save.setFixedHeight(50)
        self.btn_save.clicked.connect(self.save_config)
        self.layout.addWidget(self.btn_save)
        
        self.layout.addStretch()
        
        self.load_config()

    def create_label(self, text, subtext):
        wid = QWidget()
        lay = QVBoxLayout(wid)
        lay.setContentsMargins(0,0,0,0)
        lay.setSpacing(2)
        l1 = QLabel(text)
        l1.setStyleSheet("font-size: 14px; color: #e2e8f0; font-weight: bold;")
        l2 = QLabel(subtext)
        l2.setStyleSheet("font-size: 11px; color: #64748b;")
        lay.addWidget(l1)
        lay.addWidget(l2)
        return wid

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    self.spin_workers.setValue(data.get("workers", 8))
                    self.spin_batch.setValue(data.get("batch_size", 64))
                    self.spin_mcts.setValue(data.get("mcts_sims", 25))
            except:
                pass

    def save_config(self):
        data = {
            "workers": self.spin_workers.value(),
            "batch_size": self.spin_batch.value(),
            "mcts_sims": self.spin_mcts.value()
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("Configuration saved!")
