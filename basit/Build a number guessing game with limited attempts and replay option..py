
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 5)

# Take a number from the user
user_number = int(input("Guess a number between 1 and 5: "))

# Check whether the user's number matches the random number
while user_number != random_number:

    print("Wrong Guess! You Lose. Try Again.")

    user_number = int(input("Enter another number: "))

# If the number matches
if user_number == random_number:
    print("Congratulations! You Win!")
