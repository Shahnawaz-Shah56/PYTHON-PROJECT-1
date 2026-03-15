class Student:
    def __init__(self, name, age, grade):
          self.name = name
          self.age = age
          self.grade = grade
        
    def introduce(self):
            print(f"I am {self.name}, {self.age} years of old and my grade is {self.grade}")

S1 = Student("shahnawaz", 18, "12th")
print(S1.introduce())