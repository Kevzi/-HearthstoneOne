"""Geometry Calibration Tool - Displays test points on overlay."""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
from PyQt6.QtCore import Qt, QPointF

from overlay.geometry import HearthstoneGeometry

class CalibrationOverlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.geometry_calc = HearthstoneGeometry()
        
        self.setWindowTitle("Geometry Calibration")
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        if QApplication.primaryScreen():
            screen_geo = QApplication.primaryScreen().geometry()
            self.setGeometry(screen_geo)
            self.geometry_calc.resize(screen_geo.width(), screen_geo.height())
        else:
            self.setGeometry(0, 0, 1920, 1080)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Colors
        red = QColor(255, 0, 0, 200)
        green = QColor(0, 255, 0, 200)
        blue = QColor(0, 100, 255, 200)
        yellow = QColor(255, 255, 0, 200)
        
        font = QFont("Arial", 12, QFont.Weight.Bold)
        painter.setFont(font)
        
        # === OPPONENT HERO ===
        pos = self.geometry_calc.get_hero_pos(is_opponent=True)
        self._draw_point(painter, pos, red, "OPP HERO")
        
        # === PLAYER HERO ===
        pos = self.geometry_calc.get_hero_pos(is_opponent=False)
        self._draw_point(painter, pos, green, "MY HERO")
        
        # === OPPONENT BOARD (simulate 3 minions) ===
        for i in range(3):
            pos = self.geometry_calc.get_opponent_minion_pos(i, 3)
            self._draw_point(painter, pos, red, f"OPP {i+1}")
        
        # === PLAYER BOARD (simulate 3 minions) ===
        for i in range(3):
            pos = self.geometry_calc.get_player_minion_pos(i, 3)
            self._draw_point(painter, pos, green, f"MY {i+1}")
        
        # === PLAYER HAND (simulate 5 cards) ===
        for i in range(5):
            pos = self.geometry_calc.get_hand_card_pos(i, 5)
            self._draw_point(painter, pos, yellow, f"HAND {i+1}")
        
        # === END TURN BUTTON ===
        pos = self.geometry_calc.get_turn_button_pos()
        self._draw_point(painter, pos, blue, "END TURN")

    def _draw_point(self, painter, pos, color, label):
        point = QPointF(float(pos.x), float(pos.y))
        
        # Circle
        pen = QPen(color, 3)
        painter.setPen(pen)
        painter.setBrush(QColor(color.red(), color.green(), color.blue(), 80))
        painter.drawEllipse(point, 20, 20)
        
        # Label
        painter.setPen(QPen(Qt.GlobalColor.white))
        painter.drawText(int(pos.x - 30), int(pos.y - 25), label)

def main():
    app = QApplication(sys.argv)
    window = CalibrationOverlay()
    window.show()
    print("Calibration overlay running. Close window to exit.")
    print("Adjust values in overlay/geometry.py based on what you see.")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
