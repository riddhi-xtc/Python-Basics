
import random

print("================================")
print("       NUMBER GUESSING GAME")
print("================================")

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
    guess = int(input("\nEnter your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("\nCONGRATULATIONS! YOU WON!")
        print("Correct number:", secret_number)
        print("Total attempts:", attempts)
        break

print("================================")
print("       GAME OVER!")