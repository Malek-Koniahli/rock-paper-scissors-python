import random


def determine_winner(user_choice, computer_choice):
    """Determine the winner of a rock-paper-scissors game."""
    if user_choice == computer_choice:
        return "draw"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"


def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Options: Rock, Paper, Scissors")
    print("Type 'exit' to quit the game\n")
    
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    draws = 0
    
    while True:
        user_choice = input("Your choice (Rock, Paper, Scissors): ").strip().lower()
        
        if user_choice == "exit":
            print("\nThank you for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}, Draws: {draws}")
            break
        
        if user_choice not in choices:
            print("Invalid choice, please try again.\n")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice.capitalize()}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "draw":
            print("It's a draw!\n")
            draws += 1
        elif result == "user":
            print("You win!\n")
            user_score += 1
        else:
            print("Computer wins!\n")
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}, Draws: {draws}\n")


if __name__ == "__main__":
    main()

