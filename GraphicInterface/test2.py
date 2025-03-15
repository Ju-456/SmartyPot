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
            "Basilic": ("Difficulté: ⭐⭐", "Eau: 💧💧"),
            "Menthe": ("Difficulté: ⭐", "Eau: 💧"),
            "Fraise": ("Difficulté: ⭐⭐⭐", "Eau: 💧💧💧"),
            "Feuilles": ("Difficulté: ⭐⭐", "Eau: 💧💧"),
            "Fleurs": ("Difficulté: ⭐⭐⭐", "Eau: 💧💧💧")
        }

        for name in self.plant_data.keys():
            button = QPushButton(name)
            button.setStyleSheet("font-size: 14px; padding: 10px;")
            button.clicked.connect(lambda checked, n=name: self.select_plant(n))
            plants_layout.addWidget(button)
            self.plant_buttons.append(button)

        main_layout.addLayout(plants_layout)

        self.difficulty_label = QLabel("Difficulté: -")
        self.difficulty_label.setStyleSheet("font-size: 16px; margin-top: 20px;")
        main_layout.addWidget(self.difficulty_label)

        self.water_label = QLabel("Eau: -")
        self.water_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        main_layout.addWidget(self.water_label)

        self.setLayout(main_layout)

    def select_plant(self, plant_name):
        difficulty, water = self.plant_data[plant_name]
        self.difficulty_label.setText(difficulty)
        self.water_label.setText(water)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())