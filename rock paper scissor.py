import random
options = ["r", "s", "p"]


playGame = "y"

while playGame =="y":
    userchoice = False
    while not userchoice:
        userInput = input("Enter your input rock for r , paper for p , scissor for s \n").lower()
        
        if userInput in options:
            userchoice = True
        else:
            print("enter the valid value")

    computerInput = random.choice(options)

    if computerInput == userInput:
        print("The game is tie.......")
    elif userInput == "p" and computerInput == 'r':
        print("Congratulation you win......")

    elif userInput == "s" and computerInput == 'p'  :
         print("Congratulation you win......")

    elif userInput == "r"and computerInput == 's'  :
        print("Congratulation you win......")
    else:
        print("COMPUTER WINS ........")

    print(f"You choose {userInput} \n and computer choose {computerInput}")

    playGame = input("Do you want to play again? (y/n)")
print ("THANKS FOR PLAYING ....")
    