import random

def roll(sides=6):
    numRolled = random.randint(1,6)
    return numRolled

def main():
    sides = 6
    rolling = True
    while rolling:
        rollAgain = input("Ready to roll? ENTER=Roll.  Q=Quit. ")
        if rollAgain.lower() != "q":
            numRolled = roll(sides)
            print("You rolled a:", numRolled)
        else:
            rolling = False
    print("Come back again!")

main()
