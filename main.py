#MINH TRAN
#FILE NAME: main.py
#an app that will accept user input for a car, then output the data
# class Vehicle, Automobile
# variables car,year,make,model,doors,roof



class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type=vehicle_type
class Automobile(Vehicle):
    def __init__(self, vehicle_type,year,make,model,doors,roof):
        super().__init__(vehicle_type)
        self.year=year
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof
def get_input():
    year=input("Enter the year: ")
    make=input("Enter the maker: ")
    model=input("Enter the model: ")
    doors=input("Enter the doors (2 or 4): ")  
    roof=input("Enter the roof(solid or sun roof): ")
    return year,make,model,doors,roof
def main():
    print("Enter info of your car")
    year,make,model,doors,roof = get_input()
    car = Automobile("car",year,make,model,doors,roof)
    print("Car info")
    print("Vehicle type:",car.vehicle_type)
    print("Year:",car.year)
    print("Make:",car.make)
    print("Model:",car.model)
    print("Number of doors:",car.doors)
    print("Type of roof:",car.roof)

main()