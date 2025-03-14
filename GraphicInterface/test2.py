from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtGui import QPixmap
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sélection de Plantes")
        self.setGeometry(100, 100, 600, 400)

        main_layout = QVBoxLayout()

        self.label = QLabel("Sélectionner votre type de plantes :")
        self.label.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(self.label)

        plants_layout = QHBoxLayout()

        self.plant_buttons = []
        self.plant_data = {
            "Basilic": ("Eau: 💧💧", "Température: 22°C", "Qualité de l'air: 😊"),
            "Menthe": ("Eau: 💧", "Température: 18°C", "Qualité de l'air: 😀"),
            "Fraise": ("Eau: 💧💧💧", "Température: 20°C", "Qualité de l'air: 😁"),
            "Feuilles": ("Eau: 💧💧", "Température: 19°C", "Qualité de l'air: 🙂"),
            "Fleurs": ("Eau: 💧💧💧", "Température: 23°C", "Qualité de l'air: 😊")
        }

        for name in self.plant_data.keys():
            button = QPushButton(name)
            button.setStyleSheet("font-size: 14px; padding: 10px;")
            button.clicked.connect(lambda checked, n=name: self.select_plant(n))
            plants_layout.addWidget(button)
            self.plant_buttons.append(button)

        main_layout.addLayout(plants_layout)

        self.info_layout = QVBoxLayout()
        
        self.water_label = QLabel("Eau: -")
        self.water_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.info_layout.addWidget(self.water_label)

        self.temp_label = QLabel("Température: -")
        self.temp_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.info_layout.addWidget(self.temp_label)

        self.air_quality_label = QLabel("Qualité de l'air: -")
        self.air_quality_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.info_layout.addWidget(self.air_quality_label)

        main_layout.addLayout(self.info_layout)
        self.setLayout(main_layout)

    def select_plant(self, plant_name):
        water, temperature, air_quality = self.plant_data[plant_name]
        self.water_label.setText(water)
        self.temp_label.setText(temperature)
        self.air_quality_label.setText(air_quality)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())