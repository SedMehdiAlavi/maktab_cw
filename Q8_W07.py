class Employee:
    def __init__(self , name = None , salary = None ):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + other.name , self.salary + other.salary)

    def __eq__(self , other):
        return self.name == other.name and self.salary == other.salary

    def __str__(self):
        return f"Name : {self.name} Salary : {self.salary}"

    def __del__(self) :
        print(f"{self.name} deleted from system")

employee1 = Employee("fatemeh" , 2800)
employee2 = Employee("sadat" , 1820)
print(employee1 , employee2)
print(employee1 + employee2)
