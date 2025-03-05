#Simple  number guessing game
import random
num = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))
if guess == num:
    print("Congratulations! You guessed the number!")
else:
    print(f"Wrong! The number was {num}.")
# End of guess_number.py
