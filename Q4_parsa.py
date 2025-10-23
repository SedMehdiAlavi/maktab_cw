class Product :
    def __init__(self , name =  None , price = None , quantity = int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        if self.name == other.name:
            return Product(self.name , self.price , self.quantity + other.quantity)

    def __eq__(self , other):
        return self.name == other.name and self.price == other.price and self.quantity == other.quantity

    def __str__(self):
        return f"Name : {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"

    def __del__(self):
        print("Deleted product")

product1 = Product("laptop" , "35,000,000" , 10)
product2 = Product("laptop2" , "35,000,000" , 10)
print(product1)
print(product1 + product2)
