score = 100

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 75 and score < 90:
    print("Grade B")
elif score >= 60 and score < 75:
    print("Grade C")
elif score < 60 and score > -1:
    print("fail")
else:
    print("numbers not valid")

for i in range(11):
        if i == 5:
            continue
        print(i)