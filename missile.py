class Missile:
    def __init__(self, name, range_km, speed_mach):
        self.name = name
        self.range_km = range_km
        self.speed_mach = speed_mach

    def launch(self):
        return f"{self.name} launched at Mach {self.speed_mach}!"

    def __str__(self):
        return f"{self.name} | Range: {self.range_km} km | Speed: Mach {self.speed_mach}"
