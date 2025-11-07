import random

user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors! Best of 3 rounds.\n")

for round_num in range(1, 4):
    print("Round", round_num)
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    user_choice = input("Enter your choice (1, 2, or 3): ")

    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1, 2, or 3.\n")
        continue

    user_choice = int(user_choice)
    computer_choice = random.randint(1, 3)

    if user_choice == 1:
        user_move = "Rock"
    elif user_choice == 2:
        user_move = "Paper"
    else:
        user_move = "Scissors"

    if computer_choice == 1:
        computer_move = "Rock"
    elif computer_choice == 2:
        computer_move = "Paper"
    else:
        computer_move = "Scissors"

    print("You chose:", user_move)
    print("Computer chose:", computer_move)

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

print("----- Final Results -----")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("You are the overall winner!")
elif user_score < computer_score:
    print("Computer wins the best of three!")
else:
    print("It's an overall tie!")
