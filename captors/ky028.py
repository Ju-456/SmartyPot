import adafruit_dht
import board

# Crée une instance du capteur (utilise D4 pour GPIO4)
dht_device = adafruit_dht.DHT22(board.D4)

def getTemperature():
    """Récupère la température du capteur DHT22."""
    try:
        temperature = dht_device.temperature
        if temperature is None:
            raise ValueError("Température non valide")
        return temperature
    except (RuntimeError, ValueError) as e:
        print(f"Erreur de lecture de la température : {e}")
        return None  # Retourne None en cas d'erreur

def getHumidity():
    """Récupère l'humidité du capteur DHT22."""
    try:
        humidity = dht_device.humidity
        if humidity is None:
            raise ValueError("Humidité non valide")
        return humidity
    except (RuntimeError, ValueError) as e:
        print(f"Erreur de lecture de l'humidité : {e}")
        return None  # Retourne None en cas d'erreur
