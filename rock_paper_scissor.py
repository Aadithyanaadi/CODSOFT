import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Choose 'rock', 'paper', or 'scissors'. Type 'exit' to quit.")

    user_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("\nEnter your choice: ").lower()
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
