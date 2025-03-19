from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtGui import QFont, QPixmap, QPalette, QBrush, QIcon
from PySide6.QtCore import Qt, QTimer
import sys
import os

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sélection de Plantes")
        self.setGeometry(100, 100, 600, 402)
        self.set_background_image()
        self.choosed_plant = ""

        main_layout = QVBoxLayout()

        plants_layout = QHBoxLayout()
        self.plant_buttons = []
        self.plant_data = {
            "Basilic": ("Difficulté: ⭐⭐", "Eau: 💧💧"),
            "Menthe": ("Difficulté: ⭐", "Eau: 💧"),
            "Fraise": ("Difficulté: ⭐⭐⭐", "Eau: 💧💧💧"),
            "orchidees": ("Difficulté: ⭐⭐", "Eau: 💧💧"),
            "Begonias": ("Difficulté: ⭐⭐⭐", "Eau: 💧💧💧")
        }

        self.label = QLabel("Sélectionner votre type de plantes :")
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet("""font-size: 20px; 
                                 font-weight: bold; 
                                 color: green; 
                                 text-align: center; 
                                 margin-top: 20px;""")
        main_layout.addWidget(self.label)

        plants_layout = QHBoxLayout()

        self.plant_images = {
            "Basilic": "basilic.png",
            "Menthe": "menthe.png",
            "Fraise": "fraise.png",
            "orchidees": "orchidees.png",
            "Begonias": "begonias.png"
        }

        self.plant_buttons = []

        for name, image_file in self.plant_images.items():
            button = QPushButton("")
            button.setFixedSize(88, 88)
            image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), image_file)
            print(f"Le chemin de l'image pour {name} est : {image_path}")
            button.setStyleSheet(f"""
                QPushButton {{
                border-radius: 44px;
                background-image: url({image_path});
                background-position: center;
                background-repeat: no-repeat;
            }}
        """)

            button.clicked.connect(lambda checked, n=name: self.select_plant(n))
            plants_layout.addWidget(button)
            self.plant_buttons.append(button)

        main_layout.addLayout(plants_layout)

        self.difficulty_label = QLabel("Difficulté: -")
        self.difficulty_label.setFont(QFont("Arial", 18))
        self.difficulty_label.setStyleSheet("font-size: 17px; color: green;")
        main_layout.addWidget(self.difficulty_label)

        self.water_label = QLabel("Eau: -")
        self.water_label.setFont(QFont("Arial", 18))
        self.water_label.setStyleSheet("font-size: 17px; color: green;")
        main_layout.addWidget(self.water_label)

        self.next_button = QPushButton("Suivant")
        self.next_button.setFont(QFont("Arial", 10))
        self.next_button.setFixedSize(100, 50)
        self.next_button.setVisible(False)
        self.next_button.clicked.connect(self.open_new_page)
        main_layout.addWidget(self.next_button)

        self.setLayout(main_layout)

    def set_background_image(self):
        """Applique une image de fond à la fenêtre principale."""
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "background.png")
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            print("Erreur : l'image de fond n'a pas pu être chargée.")
            return

        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)

    def set_background_image_for_window(self, window):
        """Applique une image de fond à une fenêtre donnée."""
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "background.png")
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            print("Erreur : l'image de fond n'a pas pu être chargée.")
            return

        palette = window.palette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        window.setPalette(palette)

    def select_plant(self, plant_name):
        self.choosed_plant = plant_name
        difficulty, water = self.plant_data[plant_name]
        self.difficulty_label.setText(difficulty)
        self.water_label.setText(water)
        self.next_button.setVisible(True)

    def open_new_page(self):
        """Ouvre une nouvelle page avec des informations sur la plante sélectionnée."""
        self.new_window = QWidget()
        self.new_window.setGeometry(100, 100, 600, 402)
        self.set_background_image_for_window(self.new_window)

        layout = QVBoxLayout()

        info_title = f"A savoir sur... {self.choosed_plant}"
        label_info = QLabel(info_title)
        label_info.setFont(QFont("Arial", 20, QFont.Bold))
        label_info.setStyleSheet("font-size: 20px; font-weight: bold; color: green; margin-top: 10px;")
        layout.addWidget(label_info)

                # Texte descriptif selon la plante choisie
        details = ""

        if self.choosed_plant == "Basilic":
            details = """• <b>Exposition :</b> Soleil ou mi-ombre.<br>
        • <b>Arrosage :</b> 1 fois/jour en été, sans excès.<br>
        • <b>Sol :</b> Terreau riche et bien drainé.<br>
        • <b>Entretien :</b> Tailler régulièrement.<br>
        • <b>Engrais :</b> Compost toutes les 2 semaines.<br>"""

        elif self.choosed_plant == "Menthe":
            details = """• <b>Exposition :</b> Soleil léger.<br>
        • <b>Arrosage :</b> 2 fois/semaine.<br>
        • <b>Sol :</b> Humide et drainé.<br>
        • <b>Entretien :</b> Couper les tiges trop longues.<br>
        • <b>Engrais :</b> Peu d’engrais nécessaire.<br>"""

        elif self.choosed_plant == "Fraise":
            details = """• <b>Exposition :</b> Soleil ou mi-ombre.<br>
        • <b>Arrosage :</b> 1 fois/jour en été.<br>
        • <b>Sol :</b> Terreau riche et bien drainé.<br>
        • <b>Entretien :</b> Retirer feuilles jaunies et stolons.<br>
        • <b>Engrais :</b> Compost au printemps et après récolte.<br>"""

        elif self.choosed_plant == "Orchidees":
            details = """• <b>Exposition :</b> Mi-ombre.<br>
        • <b>Arrosage :</b> Modéré.<br>
        • <b>Sol :</b> Riche en humus.<br>
        • <b>Entretien :</b> Tailler les feuilles mortes.<br>
        • <b>Engrais :</b> Compost naturel conseillé.<br>"""

        elif self.choosed_plant == "Begonias":
            details = """• <b>Exposition :</b> Soleil direct.<br>
        • <b>Arrosage :</b> Régulier, mais éviter l’excès d’eau.<br>
        • <b>Sol :</b> Léger et bien drainé.<br>
        • <b>Entretien :</b> Enlever les fleurs fanées.<br>
        • <b>Engrais :</b> Engrais pour fleurs 1 fois/mois.<br>"""

        # Ajouter les détails au layout
        label_details = QLabel(details)
        label_details.setFont(QFont("Arial",15))
        label_details.setStyleSheet("""font-size: 16px; 
                                 color: green; 
                                 text-align: center; 
                                 margin-top: 10px;""")
        label_details.setTextFormat(Qt.RichText)  # Pour interpréter le texte en HTML car en gras
        layout.addWidget(label_details)

        back_button = QPushButton("Retour")
        back_button.setFont(QFont("Arial", 10))
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.close_new_page)
        layout.addWidget(back_button)

        self.new_window.setLayout(layout)
        self.new_window.show()
        self.hide()

    def close_new_page(self):
        """Ferme la fenêtre d'informations et revient à l'écran principal."""
        self.new_window.close()
        self.show()

    def quit_application(self):
        """Quitte l'application."""
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
