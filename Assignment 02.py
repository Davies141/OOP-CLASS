#01
class Employee:
    def __init__(self, name, id, salary):
#Double underscores"__" are used declare attributes as private this prevents direct access from the outside class 
        self.__name = name
        self.__id = id
        self.__salary = salary
# Public getter methods (`get_name`, `get_id`, `get_salary`) are provided to access and update the private variables. This allows controlled access to the variables.
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_salary(self):
        return self.__salary
# The set_salary function ensures that the salary is never a negative number.
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")
#Her encapsulation helps maintain data integrity and prevents unauthorized access to sensitive employee information.

#02
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"Starting engine of {self.make} {self.model}")
        return "Engine started"

# This "car" derived class inherits its attributes from the "Vehicle" base class and override the `start_engine` method to provide implementations.
class Car(Vehicle):
    def start_engine(self):
        print(f"Starting engine of {self.make} {self.model}")
        return "Car engine started"

# This "Truck" derived class inherits its attributes from the "Vehicle" base class and override the `start_engine` method to provide specific implementations.
class Truck(Vehicle):
    def start_engine(self):
        print(f"Starting engine of {self.make} {self.model}")
        return "Truck engine started"

# Function for demonstrating polymorphism
# The "start_any_vehicle" function demonstrates polymorphism by taking any vehicle object and calling its `start_engine`.
def start_any_vehicle(vehicle):
    print(vehicle.start_engine())

# function for demonstration purpose
car = Car("Mercedes", "E250")
truck = Truck("Scania", "4-series")

# Demonstrating polymorphism
start_any_vehicle(car)
start_any_vehicle(truck)
