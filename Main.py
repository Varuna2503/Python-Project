import os
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("🎮 Game Menu")
        print("1. Enter 1 to play 'Rock, Paper, Scissors' ")
        print("2. Enter 2 to play 'Snake Game' ")
        print("3. Enter 3 to Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            subprocess.run(["python3", "rps.py"])
        elif choice == "2":
            subprocess.run(["python3", "snakes.py"])
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
