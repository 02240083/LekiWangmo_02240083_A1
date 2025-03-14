import random as r

secret_num = r.randint(1,10)
max_attempt = 3

def welcome_message():
    print("\nwelcome to the Number Guessing Game!")
    print(f"You have {max_attempt} attempts to guess the correct number.")

def guess_recursive(attempt_left):
    guess = int(input("Guess the number between 1 and 10 : "))
    if guess == secret_num:
        print("Congraduation! You guess is correct.")
    else:
        if attempt_left > 1:
            guess_recursive(attempt_left - 1)
        else:
            print (f"\n Sorry, you couldn't guess the number. The correct number was {secret_num}")

welcome_message()
guess_recursive(max_attempt)




