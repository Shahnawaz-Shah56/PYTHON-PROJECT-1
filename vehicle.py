class Vehicle:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def info(self):
        print(f"this is {self.name} and its model is {self.brand}")



class Car(Vehicle):
    def __init__(self, name, brand, model):
        super().__init__(name, brand)
        self.model = model

    def full_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
        
Car1 = Car("fortuner","toyota",2024)
print(Car1.brand)
print(Car1.name)
print(Car1.model)