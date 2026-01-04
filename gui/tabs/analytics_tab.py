from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame, 
                             QLabel, QGridLayout)
from PyQt6.QtCore import Qt
import pyqtgraph as pg

class AnalyticsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(20)
        
        # History for plots
        self.loss_history = []
        self.wr_history = []
        self.iterations = []
        
        # Charts Grid
        charts_layout = QGridLayout()
        
        # 1. Loss Plot
        self.loss_plot_wid = self.create_plot_card("Neural Network Loss", "Loss", "lower is better", "#3b82f6")
        self.loss_plot = self.loss_plot_wid.plot_widget
        self.loss_curve = self.loss_plot.plot(pen=pg.mkPen(color='#3b82f6', width=3), symbol='o', symbolSize=8, symbolBrush='#3b82f6')
        charts_layout.addWidget(self.loss_plot_wid, 0, 0)
        
        # 2. Winrate Plot
        self.wr_plot_wid = self.create_plot_card("AI (Player 2) Winrate", "Winrate %", "higher is better", "#10b981")
        self.wr_plot = self.wr_plot_wid.plot_widget
        self.wr_plot.setYRange(0, 100)
        self.wr_curve = self.wr_plot.plot(pen=pg.mkPen(color='#10b981', width=3), symbol='o', symbolSize=8, symbolBrush='#10b981')
        charts_layout.addWidget(self.wr_plot_wid, 0, 1)
        
        # 3. Buffer Size
        self.buffer_plot_wid = self.create_plot_card("Replay Buffer Size", "Samples", "data accumulation", "#a855f7")
        self.buffer_plot = self.buffer_plot_wid.plot_widget
        self.buffer_curve = self.buffer_plot.plot(pen=pg.mkPen(color='#a855f7', width=3), symbol='o', symbolSize=8, symbolBrush='#a855f7')
        self.buffer_history = []
        charts_layout.addWidget(self.buffer_plot_wid, 1, 0, 1, 2) # Span full width
        
        self.layout.addLayout(charts_layout)
        
        # Load existing history if available
        self.load_initial_history()
        
    def create_plot_card(self, title, axis_label, subtitle, color):
        card = QFrame()
        card.setProperty("class", "card")
        layout = QVBoxLayout(card)
        
        header = QHBoxLayout()
        t_label = QLabel(title)
        t_label.setStyleSheet(f"font-weight: bold; font-size: 14px; color: {color};")
        s_label = QLabel(subtitle)
        s_label.setStyleSheet("color: #64748b; font-size: 11px;")
        
        header.addWidget(t_label)
        header.addStretch()
        header.addWidget(s_label)
        layout.addLayout(header)
        
        plot = pg.PlotWidget()
        plot.setBackground('transparent')
        plot.showGrid(x=True, y=True, alpha=0.3)
        plot.setLabel('left', axis_label)
        plot.setLabel('bottom', 'Iteration')
        plot.getAxis('left').setPen(color="#94a3b8")
        plot.getAxis('bottom').setPen(color="#94a3b8")
        layout.addWidget(plot)
        
        card.plot_widget = plot
        return card

    def load_initial_history(self):
        """Try to load history from JSON to avoid empty charts on restart."""
        import json
        import os
        history_path = "training_history.json"
        if os.path.exists(history_path):
            try:
                with open(history_path, 'r') as f:
                    history = json.load(f)
                    for entry in history:
                        self.iterations.append(entry.get("iteration", 0))
                        self.loss_history.append(entry.get("avg_loss", 0.0))
                        
                        winners = entry.get("winners", {})
                        total = sum(winners.values())
                        wr = (winners.get("2", 0) / total * 100) if total > 0 else 0
                        # Try int key if str fails
                        if total == 0:
                            wr = (winners.get(2, 0) / sum(winners.values()) * 100) if sum(winners.values()) > 0 else 0
                            
                        self.wr_history.append(wr)
                        self.buffer_history.append(entry.get("buffer_size", 0))
                
                self.refresh_plots()
            except Exception as e:
                print(f"Error loading analytics history: {e}")

    def refresh_plots(self):
        if self.iterations:
            self.loss_curve.setData(self.iterations, self.loss_history)
            self.wr_curve.setData(self.iterations, self.wr_history)
            self.buffer_curve.setData(self.iterations, self.buffer_history)

    def update_data(self, stats):
        """Update the UI with real training statistics."""
        iteration = stats.get("iteration", 0)
        winners = stats.get("winners", {})
        loss = stats.get("avg_loss", 0.0)
        buffer_size = stats.get("buffer_size", 0)
        
        # Calculate winrate for P2
        total_games = sum(winners.values())
        wr_p2 = (winners.get(2, 0) / total_games * 100) if total_games > 0 else 0
        
        # Store Data
        self.iterations.append(iteration)
        self.loss_history.append(loss)
        self.wr_history.append(wr_p2)
        self.buffer_history.append(buffer_size)
        
        # Update Curves
        self.refresh_plots()
