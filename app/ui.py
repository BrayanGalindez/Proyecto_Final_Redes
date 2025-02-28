# ui_temperature.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class TemperatureUI(QWidget):
    def __init__(self):
        super().__init__()

        # Widget y Layout
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Etiqueta para mostrar la temperatura
        self.temperature_label = QLabel("Esperando datos...", self)
        self.temperature_label.setAlignment(Qt.AlignCenter)  # Centrado de texto
        self.temperature_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #fff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 8px;
        """)
        self.layout.addWidget(self.temperature_label)

        self.setStyleSheet("""
            background-color: #34495e;
            border-radius: 12px;
        """)
