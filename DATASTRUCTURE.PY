favfoods = ["rice", "icecream", "biryani", "kanti", "meat"]
favfoods.append("seekkabab")
favfoods.remove("icecream")
print(favfoods)
print(favfoods[::-1])

Myself = {
    "name": "shahnawaz",
    "age": 18,
    "job":"student",
    "city":"kasmir"
}

for key, value in Myself.items():
    print(f"{key}: {value}")

squares=[]
squares = [i**3 for i in range(1,11)]
print(squares)


countries = ("paksitan", "china", "japan","japan", "palestine", "saudia arabia")

removeduplicate =  list(set(countries))
print(removeduplicate)