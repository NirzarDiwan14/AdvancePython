class Car:
    def __init__(self,make: str,model: str,year: int):
        self.make = make.title()
        self.model = model.title()
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def details(self):
        return {
            "Make": self.make,
            "Model": self.model,
            "Year": self.year
        }

car1 = Car("hyundai", "verna", 2023)
car2 = Car("toyota", "fortuner", 2024)

print(car1)
print(car2)

print(car1.details)
print(car2.details)



        