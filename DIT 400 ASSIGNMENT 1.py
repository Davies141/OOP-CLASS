#The car class defines the blueprint for creating car objects.
class Car:
# The car class has atrributes: make, model, year and color.
#Attributes are Variables that store data within an object.
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
#Is a method used to print the car's details.
#A methods is a functions associated with a class. 
# Methods define the behavior of objects of that class.
    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
#Method to update the color of a car 
    def update_color(self, new_color):
        self.color = new_color

# Creating 3 car (objects) and asigning them with attributes.
# Objects are Instances of a class, they have their own unique values for the attributes defined in the class. 
#car1, car2 and car3 are instances of the "Car" class, representing individual cars.
car1 = Car("Toyota", "Prado", 2009, "Blue")
car2 = Car("Toyota", "Mark x", 2016, "black")
car3 = Car("Tesla", "Model s", 2021, "White")

# Method to display (print) details of the 3 car objects.
car1.display_details()
car2.display_details()
car3.display_details()

# Updating the color of one car and displaying the updated details
car1.update_color("Blue")
car1.display_details()

def create_car_from_input():
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = int(input("Enter the year of the car: "))
    color = input("Enter the color of the car: ")

    new_car = Car(make, model, year, color)
    new_car.display_details()

# This function prompts the user to enter car details and creates a new `Car` object with those values.
create_car_from_input()