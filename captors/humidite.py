import RPi.GPIO as GPIO

# Définition du GPIO connecté au capteur FC-28 (sortie DO)
DO_PIN = 26

# Configuration du GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DO_PIN, GPIO.IN)

def get_soil_humidity():
    """
    Vérifie l'humidité du sol et renvoie un message.
    :param PIN: Le numéro du GPIO connecté au capteur d'humidité.
    :return: str : Message de l'humidité du sol (sec ou humide)
    """
    soil_humidity = GPIO.input(26)  # Lit l'état du capteur d'humidité du sol
    if soil_humidity == GPIO.HIGH:
        return "Sol sec"
    else:
        return "Sol humide."
