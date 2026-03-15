import random

secret = random.randint(1,100)
print(secret)

attempts = 0

try:
    while True:
        guess = int(input("guess the number:"))
        attempts += 1

        if attempts <= 3 and guess == secret:
             print("amazing")
        elif attempts <= 6 and guess == secret:
             print("good job")
        elif attempts > 6:
             print("keep practicing")
             attempts = 0
        print(attempts)

        if guess > secret:
            print("Sorry number you guessed is higher than the random number")
        elif guess < secret:
            print("Sorry number you guess is lower than the random number")
        elif guess == secret:
        
            print(f"Congratulations you guessed the right number. You got it in {attempts}")

            reset = input("Do you wanna play the game again:")
            if reset == "yes":
                 attempts = 0
                 guess = int(input("guess the number:"))
            elif reset == "no":
                 print("Goodbye")
            break

except ValueError:
            print("Please enter the correct input. Only integers allowed as inputs")

        


