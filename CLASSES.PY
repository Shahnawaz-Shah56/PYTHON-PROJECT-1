# class car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
        

# car1 = car("suzuki", "alto800", 2024, 60000)
# print(car1.brand,car1.model, car1.price)


# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

# car1 = Car("suzuki", "alto800", 60000)
# print(car1.brand, car1.model, car1.price)






















class Student:

    collage = "GDC Pulwama"
    def __init__(self, name, marks):

        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
         print("hello students this is your result time hope for the best")
    def avg (self):
            sum = 0
            for val in self.marks:
                sum += val
            print("hi",self.name, "your score is:",sum/3)

S1 = Student("karan", [99, 66, 59])
S1.hello()
S1.avg()

        