# def checkevenodd(a):
#     if a%2 == 0:
#         print(a ,"is even number")
#     else:
#         print(a ,"is odd number")

# checkevenodd(3)

def introduce(name, age, city="unknown"):
    return f"Hi! I am {name}, {age} years old from {city}"

output = introduce("shahnawaz", 20)
print(output)

def calculateArea(length, width):
    return length * width
print(calculateArea(3,2))