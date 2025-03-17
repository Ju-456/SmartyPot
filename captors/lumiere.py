import smbus
import time

# Adresse I2C du capteur BH1750
BH1750_ADDRESS = 0x23

# Commandes de mesure
CONTINUOUS_HIGH_RES_MODE = 0x10  # Mode haute résolution (1 lux, mesure continue)

class BH1750:
    def __init__(self, bus=1, address=BH1750_ADDRESS):
        self.bus = smbus.SMBus(bus)
        self.address = address

    def get_light_level(self):
        self.bus.write_byte(self.address, CONTINUOUS_HIGH_RES_MODE)
        time.sleep(0.2)  # Attente pour la mesure
        data = self.bus.read_i2c_block_data(self.address, 2)
        lux = (data[0] << 8 | data[1]) / 1.2
        return lux

# Fonction pour obtenir la luminosité
def get_light():
    sensor = BH1750()
    return sensor.get_light_level()

# Exemple d'utilisation
if __name__ == "__main__":
    print(f"Luminosité: {get_light():.2f} lux")
