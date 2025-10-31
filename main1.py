# random-> to generate Random number between 1 and 10
# random.randrange(1, 10) → returns 1 to 9
# random.randint(1, 10) → returns 1 to 10
import random 
secret = random.randint(1, 10)  
attempts = 0

print(" Guess the number (between 1 and 10):")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print(f" Correct! The number was {secret}. You guessed it in {attempts} tries.")
        break
    elif guess < secret:
        print(" Too low! Try again.")
    else:
        print(" Too high! Try again.")
