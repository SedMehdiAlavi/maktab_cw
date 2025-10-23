class Car:
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} , {self.model} , {self.price}"

    def __eq__(self , other):
        if isinstance(other , Car):
            return self.brand == other.brand and self.model == other.model

    def __add__(self , other):
        return Car(self.brand , self.model , self.price + other.price)

    def __del__(self):
        print(f"{self.brand} deleted . ")

car1 = Car("saipa" , "peraid" , 200)
car2 = Car( "irankhodro" , "pejo" , 400)

print(car1)
print(car2)
print(car1 + car2)
print(car1 == car2)

