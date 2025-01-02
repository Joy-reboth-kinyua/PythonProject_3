import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print('too high!')
        else:
            print("congratulations! You guessed the number.")
            break
    except ValueError:
       print("please enter a valid number")



