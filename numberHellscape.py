# Number Guessing game 
# Made by Chizu (Joanne) -- May 16th 2025

#Importing proper modules
import random
# Function to make text pink using ANSI escape codes 
def pink(text):
    return f"\033[38;2;255;105;180m{text}\033[0m"

# Introducing game, asking user name.
print("\033[31m🔥Welcome to Joanne's Number Hell!🧨\033[0m") 
input("\033[1mPress Enter to continue...\033[0m")
uName = input("What is your name, User?: ")
uName = pink(uName)

print(f"""Welcome, {uName}. The game works by randomising a number 
      between 1 and 50 and you have to guess what it is!""")
input("\033[1mPress Enter to continue...\033[0m")
print("")

# Game variables:
# Game stats
totalGames = 1
bestScore = float('inf')

# Main game loop - Generates a new number each round
while True:
#   Initialize random number
    ranNum = random.randint(1,50)
    attempts = 0
    while True:
    #   Input and Validation
        userNumStr = input("Write your guessed number: ")
        while not userNumStr.isdigit():
            print(f"Whoops! You need to input a number {uName}")
            userNumStr = input("Write your guessed number: ")
        userNum = int(userNumStr)
    #   Count how many guesses the user takes this round
        attempts += 1
    #  Condition if the number is too high/too low, correct/incorrect along with proper messages
        if userNum < ranNum:
            print(f"Too low, {uName}, try higher!")
        elif userNum > ranNum:
            print(f"Too high, {uName} ! Try lower.")
        else:
            print(f"\033[32mYou are correct! {ranNum} is the number!\033[0m")
            print(f"✨ You got it in {attempts} try(s), {uName} 🌟")
            print("")
            print("Your game stats: ")
            # Updating game stats 
            if attempts < bestScore:
                bestScore = attempts
                print("\033[32m🌸 New Best Score!\033[0m")
            # Display game stats
            print(f"\033[35m💗 Games played: {totalGames}\033[0m")
            print(f"🎀 Your best score is: {bestScore}")
            print("")
            break 
#   Ask user to try again
    while True:
        restart = input(f"Would you like to play again, {uName}? (Y/N): ").upper()
        if restart == "Y":
            totalGames += 1
            break
        elif restart == "N":
            print(f"Thank you for playing, {uName}! Hope it was fun!")
            exit()
        else:
            print("Invalid input. Exiting game")
            exit()
