def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Can't divide by zero!")

    except TypeError:
        print("please enter the numbers only")
    else:
        return result

print(divide(0,1))
print(divide(10, 2))    
print(divide(10, 0))    
print(divide(10, "a")) 



try:
    with open("missing.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found, creating it now!")
    with open("missing.txt", "w") as file:
        file.write("File created successfully!")
    print("File created")