import random

number = random.randint(1, 9)
chances = 0

while chances < 5:
    chances += 1
    guess = int(input("Enter a number from 1 to 9: "))

    if guess > number: 
        print("Your guess is too high! Pick a smaller number.")

    elif guess < number:
        print("Your guess is too low! Pick a larger number.")

    elif guess == number:
        print("Congratulations!! You Won!")
        break

if not chances < 5:
    print("You Lose! The number is", number)