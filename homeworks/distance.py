class Distance:
    units = {"cm": 0.01, "m": 1, "km": 1000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.units[self.unit]


    def __add__(self, other):
        total = self.to_meters() + other.to_meters()
        return Distance(total / self.units[self.unit], self.unit)

    def __sub__(self, other):
        result = self.to_meters() - other.to_meters()
        if result < 0:
            return "Значение не может быть отрицательным"
        return Distance(result / self.units[self.unit], self.unit)