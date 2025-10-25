class Temperature:
    def __init__(self , celsius):
        self.celsius = celsius

    @property
    def farenhait(self):
        return self.celsius * (9 / 5) + 32

    @property
    def kelvin(self):
        return self.celsius + 273

temp = Temperature(25)
print(temp.farenhait)
print(temp.kelvin)
print(temp.celsius)
