def multiply_all(*args):
    result =1
    for num in args:
        result *= num
    return result
print(multiply_all(3,4,6,3,2,6,7,3,2,6))

def intro(**kwargs):
    print(kwargs)  # it's just a dictionary! {'name': 'Shahnawaz', 'age': 18}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

intro(name="Shahnawaz", age=18, city="Kashmir",job="student")


cube = lambda x: x**3
print(cube(3))


def student_info(**kwargs):
    print(kwargs)
    for key, Value in kwargs.items():
        print(f"{key}: {Value}")
student_info(name="shah", age=18, job="student")