import random

secret = random.randint(1, 100)
attempts = 0

try:
    while True:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1

        if guess > secret:
            print("Too high! 📈")
        elif guess < secret:
            print("Too low! 📉")
        else:
            print(f"Correct! 🎉 You got it in {attempts} attempts!")

            if attempts <= 3:
                print("Amazing! 🌟")
            elif attempts <= 6:
                print("Good job! 😄")
            else:
                print("Keep practicing! 💪")

            reset = input("Play again? (yes/no): ")
            if reset == "yes":
                attempts = 0
                secret = random.randint(1, 100)
            else:
                print("Goodbye! 👋")
                break

except ValueError:
    print("Numbers only please!")