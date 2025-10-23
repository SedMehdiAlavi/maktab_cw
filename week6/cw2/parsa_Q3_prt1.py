class Car :



    def __init__(self , car_id : str , model : str , year : int ,
                 is_available : bool ):
        self.car_id = car_id
        self.model = model
        self.year = year
        self.is_available = is_available
        Car.cars.append(self)

    def rent_car(self):
        if self.is_avaliable:
            self.is_available = False


    def return_car(self):
        if not self.is_available :
            self.is_available = True

    def display_info (self) :
        # self.car_id = 1234
        # self.model = "new"
        # self.year = 1999
        # self.is_available = True
        print(f"{self.car_id} {self.model} {self.year} {self.is_available}")


class RentalAgency :

    cars = []

    def __init__(self , cars : list ):
        self.cars = cars

    def add_car(self,car):
        self.cars.append(car)
        # Car.cars.append(self)
        # return Car.cars


bmw = Car("bmw" , "new" , 125 , True)
print(bmw.display_info())
print()