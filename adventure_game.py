# Script Purpose: A text-based adventure game using functions and loops 
# to demonstrate fundamental Python concepts and GitHub Copilot integration.


import time
import sys


# ANSI color codes for terminal text formatting
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"


def console_print(text, delay=0.03):
    """Prints text to the terminal in Green with a typing effect."""
    sys.stdout.write(GREEN + BOLD) # Switch to Green
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n") # Reset color and move to next line

def forest_path(player_name):
    console_print("\n--- The Dense Forest ---")
    console_print(f"{player_name}, you walk into the trees. The air is cool, and you hear a rushing river.")
    choice = input("Do you want to 'follow' the river or 'climb' a tall tree to look around? ").lower().strip()

    if choice == "follow":
        console_print("\nYou follow the river and find a sparkling waterfall. Behind it lies the TREASURE!")
        console_print("CONGRATULATIONS! YOU WIN!")
        return True
    elif choice == "climb":
        console_print("\nYou climb the tree, but a branch breaks! You fall and sprain your ankle.")
        console_print("You are unable to continue. GAME OVER.")
        return False
    else:
        console_print("Invalid choice. You wander aimlessly and get lost.")
        return False

def cave_path(player_name):
    console_print("\n--- The Mysterious Cave ---")
    console_print(f"It's pitch black inside, {player_name}. You hear a strange dripping sound.")
    choice = input("Do you want to 'light' a torch or 'proceed' in the dark? ").lower().strip()

    if choice == "light":
        console_print("\nThe torch illuminates a hidden path leading straight to the GOLDEN TREASURE!")
        console_print("CONGRATULATIONS! YOU WIN!")
        return True
    elif choice == "proceed":
        console_print("\nYou trip over a rock in the dark and fall into a deep pit.")
        console_print("The adventure ends here. GAME OVER.")
        return False
    else:
        console_print("Fear paralyzes you. You cannot move forward.")
        return False

def start_game():
    
    console_print("***************************************")
    console_print("Welcome to THE ANCIENT TREASURE QUEST")
    console_print("***************************************")
    
    name = input("Enter your name, explorer: ")
    console_print(f"\nGreetings, {name}. Your quest is to find the hidden treasure. You will face various challenges along the way. Make your choices wisely to succeed!")
    
    while True:
        path = input("Do you want to go to the 'forest' or the 'cave'? ").lower().strip()
        
        if path == "forest":
            success = forest_path(name)
            break
        elif path == "cave":
            success = cave_path(name)
            break
        else:
            console_print("That's not a valid path. Please choose 'forest' or 'cave'.")
    
    return success

# Main Loop to handle restarting
if __name__ == "__main__":
    while True:
        result = start_game()
        if result:
            console_print("\nYou have completed your adventure successfully!")
        else:
            console_print("\nBetter luck next time on your adventure!")
        
        play_again = input("\nWould you like to try again? (yes/no): ").lower().strip()
        if play_again != "yes":
            console_print("Thanks for playing! Goodbye.")
            break