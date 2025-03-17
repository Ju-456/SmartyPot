from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QTimer
#from ky028 import *
#from lumiere import *
#from mq135 import *
#from humidite import *
import random  # Utilisé pour simuler la lecture d'un capteur
import sys
import os

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sélection de Plantes")
        self.setGeometry(100, 100, 600, 402) # Mode plein écran remplacé temporairement par la taille avec laquelle on travaille

        self.choosed_plant = ""

        main_layout = QVBoxLayout()

        # Créer le label avant d'appliquer le style
        self.label = QLabel("Sélectionner votre type de plantes :")
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet("font-size: 22px; font-weight: bold; color: green; text-align: center; margin-top: 20px;")
        main_layout.addWidget(self.label)

        plants_layout = QHBoxLayout()

        self.plant_buttons = []
        self.plant_data = {
            "Basilic": ("Difficulté: ⭐⭐", "Eau: Fréquemment"),
            "Menthe": ("Difficulté: ⭐", "Eau: Rarement"),
            "Fraise": ("Difficulté: ⭐⭐⭐", "Eau: Très Fréquemment"),
            "Feuilles": ("Difficulté: ⭐⭐", "Eau: Fréquemment"),
            "Fleurs": ("Difficulté: ⭐⭐⭐", "Eau: Très Fréquemment")
        }

        for name in self.plant_data.keys():
            button = QPushButton(name)
            button.setFont(QFont("Arial",15))
            button.setFixedSize(88, 88)  # Taille fixe des boutons
            button.setStyleSheet("""
                font-size: 14px;
                background-color: white;
                border-radius: 44px;  /* La moitié de 88px pour un bouton rond */
                border: 2px solid green;
            """)# margin-top: 20px;  /* Ajout d'un espacement au-dessus du bouton mais ça ne fonctionne pas*/

            button.clicked.connect(lambda checked, n=name: self.select_plant(n))
            plants_layout.addWidget(button)
            self.plant_buttons.append(button)

        main_layout.addLayout(plants_layout)

        self.difficulty_label = QLabel("Difficulté: -")
        self.difficulty_label.setFont(QFont("Arial",17))
        self.difficulty_label.setStyleSheet("font-size: 16px; color: green;")
        main_layout.addWidget(self.difficulty_label)

        self.water_label = QLabel("Eau: -")
        self.water_label.setFont(QFont("Arial",15))
        main_layout.addWidget(self.water_label)

        self.next_button = QPushButton("Suivant")
        self.next_button.setFont(QFont("Arial",15))
        self.next_button.setFixedSize(200, 90)
        self.next_button.setVisible(False)
        self.next_button.clicked.connect(self.open_new_page)
        main_layout.addWidget(self.next_button)

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

    def select_plant(self, plant_name):
        self.choosed_plant = plant_name  # Stocker le nom de la plante sélectionnée
        difficulty, water = self.plant_data[plant_name]
        self.difficulty_label.setText(difficulty)
        self.water_label.setText(water)
        self.next_button.setVisible(True)

    def open_new_page(self):
        # Créer une nouvelle fenêtre avec les informations sur la plante
        self.new_window = QWidget()
        self.new_window.showFullScreen()

        layout = QVBoxLayout()

        info_title = f"A SAVOIR SUR : {self.choosed_plant}"
        label_info = QLabel(info_title)
        label_info.setFont(QFont("Arial", 22, QFont.Bold))
        layout.addWidget(label_info)

        # Texte descriptif selon la plante choisie
        details = ""

        if self.choosed_plant == "Basilic":
            details = "• Exposition : Soleil ou mi-ombre.\n• Arrosage : 1 fois/jour en été, sans excès.\n• Sol : Terreau riche et bien drainé.\n• Entretien : Tailler régulièrement.\n• Engrais : Compost toutes les 2 semaines."
        elif self.choosed_plant == "Menthe":
            details = "• Exposition : Soleil léger.\n• Arrosage : 2 fois/semaine.\n• Sol : Humide et drainé.\n• Entretien : Couper les tiges trop longues.\n• Engrais : Peu d’engrais nécessaire."
        elif self.choosed_plant == "Fraise":
            details = "• Exposition : Soleil ou mi-ombre.\n• Arrosage : 1 fois/jour en été.\n• Sol : Terreau riche et bien drainé.\n• Entretien : Retirer feuilles jaunies et stolons.\n• Engrais : Compost au printemps et après récolte."
        elif self.choosed_plant == "Feuilles":
            details = "• Exposition : Mi-ombre.\n• Arrosage : Modéré.\n• Sol : Riche en humus.\n• Entretien : Tailler les feuilles mortes.\n• Engrais : Compost naturel conseillé."
        elif self.choosed_plant == "Fleurs":
            details = "• Exposition : Soleil direct.\n• Arrosage : Régulier, mais éviter l’excès d’eau.\n• Sol : Léger et bien drainé.\n• Entretien : Enlever les fleurs fanées.\n• Engrais : Engrais pour fleurs 1 fois/mois."

        # Ajouter les détails au layout
        label_details = QLabel(details)
        label_details.setFont(QFont("Arial",15))
        layout.addWidget(label_details)

        # Bouton "Retour"
        back_button = QPushButton("Retour")
        back_button.setFont(QFont("Arial", 23))
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.close_new_page)
        layout.addWidget(back_button)

        # Bouton "Valider la plante"
        validate_button = QPushButton("Valider la plante")
        validate_button.setFont(QFont("Arial", 23))
        validate_button.setFixedSize(250, 100)
        validate_button.clicked.connect(self.open_validation_page)
        layout.addWidget(validate_button)

        self.new_window.setLayout(layout)
        self.new_window.show()

        # Masquer la fenêtre principale
        self.hide()

    def close_new_page(self):
        # Fermer la fenêtre actuelle (détails de la plante)
        self.new_window.close()

        # Réafficher l'écran principal
        self.show()

    def open_validation_page(self):
        # Créer une nouvelle fenêtre de validation avec un capteur d'eau
        self.validation_window = QWidget()
        self.validation_window.showFullScreen()

        layout = QVBoxLayout()

        # Nom de la plante au centre
        plant_name_label = QLabel(self.choosed_plant)
        plant_name_label.setFont(QFont("Arial", 40, QFont.Bold))
        plant_name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(plant_name_label)

        
        # Texte dynamique pour "Capteur eau"
        self.water_sensor_label = QLabel("Capteur eau : --")
        self.water_sensor_label.setFont(QFont("Arial",15))
        self.water_sensor_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.water_sensor_label)

        # Texte dynamique pour "Capteur température"
        self.temp_sensor_label = QLabel("Température : --°C")
        self.temp_sensor_label.setFont(QFont("Arial",15))
        self.temp_sensor_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.temp_sensor_label)

        # Texte dynamique pour "Capteur humidité"
        self.humidity_sensor_label = QLabel("Humidité : --%")
        self.humidity_sensor_label.setFont(QFont("Arial",15))
        self.humidity_sensor_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.humidity_sensor_label)

        # Texte dynamique pour "Capteur lumière"
        self.light_sensor_label = QLabel("Lumière : --lux")
        self.light_sensor_label.setFont(QFont("Arial",15))
        self.light_sensor_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.light_sensor_label)

        # Ajouter un label pour la qualité de l'air
        self.air_quality_label = QLabel("Qualité de l'air : --")
        self.air_quality_label.setFont(QFont("Arial",15))
        self.air_quality_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.air_quality_label)

        # Initialisation des capteurs avant le lancement du timer
        self.update_sensors()

        # Timer pour rafraîchir les valeurs des capteurs toutes les 10 secondes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_sensors)
        self.timer.start(1000)  # 10 secondes

        # Bouton "Quitter"
        quit_button = QPushButton("Quitter")
        quit_button.setFont(QFont("Arial",15))
        quit_button.setFixedSize(650, 100)
        quit_button.clicked.connect(self.quit_application)
        layout.addWidget(quit_button)

        self.validation_window.setLayout(layout)
        self.validation_window.show()

    def update_sensors(self):
        # Simuler la mise à jour des capteurs (valeurs aléatoires)
        water_value = get_soil_humidity()  # Simuler une valeur entre 0 et 100
        temp_value = getTemperature()  # Température entre 20 et 30°C
        humidity_value = getHumidity()  # Humidité entre 40% et 60%
        if get_light() > 2000:
            lux_value = 100
        else:
            lux_value = (get_light()/2000)*100
        air_quality_value = check_air_quality()

        # Mettre à jour les labels avec les nouvelles valeurs
        self.water_sensor_label.setText(f"Capteur eau : {water_value}")
        self.temp_sensor_label.setText(f"Température : {temp_value:.2f}°C")
        self.humidity_sensor_label.setText(f"Humidité : {humidity_value:.2f}%")
        self.light_sensor_label.setText(f"Luminosité: {lux_value:.2f}%")
        self.air_quality_label.setText(f"Qualité de l'air : {air_quality_value}")

    def quit_application(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
