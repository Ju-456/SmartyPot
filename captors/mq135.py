import RPi.GPIO as GPIO
import time

# Définition du GPIO où est connecté D0
MQ135_D0 = 17  # Change selon ton branchement

# Configuration du GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ135_D0, GPIO.IN)

def check_air_quality():
    """
    Vérifie la qualité de l'air à partir du capteur MQ135 et renvoie un message.
    :return: str : Message de qualité de l'air (bonne ou mauvaise)
    """
    air_quality = GPIO.input(MQ135_D0)  # Lit l'état du capteur
    if air_quality == GPIO.LOW:
        return "mauvaise. ⚠️ "
    else:
        return "correcte. ✅"

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        while True:
            print(check_air_quality())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Arrêt du programme.")
        GPIO.cleanup()
