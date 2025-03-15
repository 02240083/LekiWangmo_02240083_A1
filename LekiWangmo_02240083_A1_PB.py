import random

# Function for the 'Guess the Number' game
import random

def guess_number():
    print("\n=== GUESS THE NUMBER GAME ===")
    lower, upper = 1, 100  # Setting range for the hidden number
    hidden_number = random.randint(lower, upper)  # Randomly selecting a number
    print(f"Guess a number between {lower} and {upper}.")
    max_attempts = 5  # Maximum attempts allowed (set to 5)
    attempts = 0  # Count user attempts
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < hidden_number:
                print("Too low! Try again. You have", max_attempts - attempts, "attempts left.")
            elif guess > hidden_number:
                print("Too high! Try again. You have", max_attempts - attempts, "attempts left.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {hidden_number}.")

# Function for the 'Rock, Paper, Scissors' game
def rock_paper_scissors():
    print("\n=== ROCK, PAPER, SCISSORS GAME ===")
    choices = ["rock", "paper", "scissors"]  # Possible choices
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}  # Winning rules
    
    # Getting number of rounds from user
    while True:
        try:
            rounds = int(input("Enter the number of rounds you want to play: "))
            if rounds <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    user_score = computer_score = tie_score = 0  # Initializing scores
    
    for _ in range(rounds):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in choices:
                break
            print("Invalid choice. Please try again.")
        
        computer_choice = random.choice(choices)  # Computer selects randomly
        print(f"Computer chooses: {computer_choice}")
        
        # Determining winner
        if user_choice == computer_choice:
            print("It's a tie!")
            tie_score += 1
        elif wins[user_choice] == computer_choice:
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"Score -> You: {user_score}, Computer: {computer_score}, Ties: {tie_score}")
    
    # Displaying final results
    print("\n=== FINAL RESULTS ===")
    print(f"Final Score -> You: {user_score}, Computer: {computer_score}, Ties: {tie_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie game!")

# Main function to handle game selection
def main():
    while True:
        print("\n=== GAME MENU ===")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Exit")
        choice = input("Select a game (1-3): ")
        
        if choice == '1':
            guess_number()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        # Asking user if they want to continue playing
        cont = input("Do you want to play again? (yes/no): ").lower()
        if cont != 'yes':
            print("Exiting... Have a great day!")
            break

# Program entry point
if __name__ == "__main__":
    main()
