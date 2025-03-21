import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sélection de Plantes")
        self.setGeometry(100, 100, 600, 402)

        # Appliquer l'image de fond via QPixmap et QPalette
        self.set_background_image()

        main_layout = QVBoxLayout()

        # Créer le label avant d'appliquer le style
        self.label = QLabel("Sélectionner votre type de plantes :")
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet("font-size: 22px; font-weight: bold; color: green; text-align: center; margin-top: 20px;")
        main_layout.addWidget(self.label)

        plants_layout = QHBoxLayout()

        # Utilisation de chemins relatifs pour les images, pcq je suis pas une collaboratrice relou ;)) 
        #current_directory = os.path.dirname(os.path.abspath(__file__))
        self.plant_data = {
            "Basilic": ("Eau: 💧💧", "Température: 22°C", "Qualité de l'air: 🙂"),
            "Menthe": ("Eau: 💧", "Température: 18°C", "Qualité de l'air: 😃"),
            "Fraise": ("Eau: 💧💧💧", "Température: 20°C", "Qualité de l'air: 😆"),#, os.path.join(current_directory, "FraisePicture.png")
            "Orchidée": ("Eau: 💧💧", "Température: 19°C", "Qualité de l'air: ☺"),
            "Begonia": ("Eau: 💧💧💧", "Température: 23°C", "Qualité de l'air: 🙂")
        }

        # Boutons pour chaque plante
        for name in self.plant_data.keys():
            button = QPushButton(name)
            button.setFixedSize(88, 88)  # Taille fixe des boutons

            button.setStyleSheet("""
                font-size: 14px;
                background-color: white;
                border-radius: 44px;  /* La moitié de 88px pour un bouton rond */
                border: 2px solid green;
            """)# margin-top: 20px;  /* Ajout d'un espacement au-dessus du bouton mais ça ne fonctionne pas*/

            button.clicked.connect(self.make_callback(name))
            plants_layout.addWidget(button)

        main_layout.addLayout(plants_layout)

        # Labels d'info
        self.water_label = QLabel("Eau: -")
        self.temp_label = QLabel("Température: -")
        self.air_quality_label = QLabel("Qualité de l'air: -")

        for label in [self.water_label, self.temp_label, self.air_quality_label]:
            label.setStyleSheet("font-size: 16px; margin-top: 10px; color: black;")
            main_layout.addWidget(label)

        self.setLayout(main_layout)

    def set_background_image(self):
        # Chemin absolu du fichier (assurez-vous que le fichier est dans ce répertoire)
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "background.png")
        
        # Vérifiez le chemin complet de l'image, print(f"Chemin de l'image : {image_path}")

        # Charger l'image en utilisant QPixmap
        pixmap = QPixmap(image_path)

        # Vérifier si l'image a bien été chargée
        if pixmap.isNull():
            print("Erreur : l'image de fond n'a pas pu être chargée.")
            return

        # Créer un QPalette et y appliquer l'image de fond
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), pixmap)
        
        # Appliquer le QPalette à la fenêtre
        self.setPalette(palette)

    def make_callback(self, plant_name):
        return lambda: self.select_plant(plant_name)

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
