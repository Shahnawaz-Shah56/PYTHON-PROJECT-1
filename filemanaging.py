from math import pi,sqrt,ceil
import random
print(sqrt(144))
print(pi)
print(ceil(7.2))

print(random.randint(1,100))


print(random.choice(["japan","pakistan",'holland','palestine','turkey']))



file = open("IDEAS.txt", "w")
file.write("Hello Shahnawaz!\n")
file.write("age:20!\n")
file.write("kashmir")
file.close()

file = open("info.txt", "r")
content = file.read()
print(content)
file.close()
