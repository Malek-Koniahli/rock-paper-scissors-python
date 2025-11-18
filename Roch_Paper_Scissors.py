import random
print("Welcome to Rock-Paper-SCISSORS!")
print("options: Rock, Paper, Scissors")
print("Type 'exit' to quit the game/n")

choices = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Your choice (Rock, Paper, Scissors): ").strip().lower()
    if user_choice == "exit":
        print("Thank you for playing!")
        break
    if user_choice not in choices:
        print("Invalid Choice, please try again./n")
        continue
    computer_choice = random.choice(choices)
    print("Computer chooses:", computer_choice)
    if user_choice == computer_choice:
        print("Draw!/n")
    elif(
        (user_choice == "rock" and
    computer_choice == "scissors") or
        (user_choice == "paper" and
    computer_choice == "rock") or
        (user_choice == "scissors" and
    computer_choice == "paper")
    ):
        print("You win!/n")
    else:
        print("Computer wins!/n")






