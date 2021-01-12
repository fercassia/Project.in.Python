from random import *

print("Bem vindo ao Jokempô!\n")

def jokenpoChoice(chosenItem):
    if chosenItem == 1:
        return "Stone"
    elif chosenItem == 2:
        return "Paper"
    elif chosenItem == 3:
        return "Scissors"
    elif chosenItem == 4:
        return "Exit"
    else:
        return "Invalid"
def jokenpo():
    newGame = True
    while(newGame):
        choiceMachine = randint(1, 3)
        choiceEntry = int(input("Entry (0.Help/1.Exit/7.New Game): \n"))
        if(choiceEntry == 1):
            newGame = False
            print("To the next! See you later!\n")
        elif(choiceEntry == 7):
            print("Play options 1. Stone\n 2. Paper\n 3. Scissors\n 4. Exit Game\n:")
            choiceUser = int(input("Entry to play (1/2/3/4): \n"))
            if (choiceUser != 4 and choiceUser > 0 and choiceUser < 4):
                if(choiceUser == choiceMachine):
                    print("Machine: " + jokenpoChoice(choiceMachine) + " || You: " + jokenpoChoice(choiceUser))
                    print("Technical tie! Let's play again!\n")
                elif(choiceUser > choiceMachine):
                    print("Machine: " + jokenpoChoice(choiceMachine) + " || You: " + jokenpoChoice(choiceUser))
                    print("Congratulations! You won!\n")
                elif(choiceUser < choiceMachine):
                    print("Machine: " + jokenpoChoice(choiceMachine) + " || You: " + jokenpoChoice(choiceUser))
                    print("Aaaaah.... what a pity, you lost!\n")
            elif choiceUser == 4:
                print("You chose to leave! To the next! See you later!\n")
                break
            else:
                print("Invalid choice, try again!")
                newGame = True

        elif(choiceEntry == 0):
            print("Welcome to the rules!\n")
            print("This game is to spend your time! It's you against the machine!\n")
            print("Stone wins from Scissors (stone knead scissors)\n")
            print("Scissors wins from paper (scissors cut the paper)\n")
            print("Paper wins from Stone (paper wraps stone)\n")
            print("If technical tie, it must be played again until the untie\n")

        else:
            print("Invalid choice! Please choose a valid option to play!\n")
jokenpo()