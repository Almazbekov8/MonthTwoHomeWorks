class Distance:
    units = {"cm": 0.01, "m": 1, "km": 1000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"