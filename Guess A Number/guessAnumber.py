import random


def isValidNum(theirInput):  # Checks to see if USER INPUT is valid (integer between 1-1000).
    if theirInput.isdigit() and 1 <= int(theirInput) <= 1000:
        return True
    else:
        return False


def main():
    randNum = random.randint(1, 1000)
    guessed_number = False
    guess = input("Guess a number.  1 to 1000.")
    num_guesses = 0
    while not guessed_number:  # While guessed_number is False:
        if not isValidNum(guess):  # If isValidNum(their guess) is False:
            guess = input("Give me a WHOLE NUMBER 1-1000 please.")
            continue  # means we'll move to the next iteration of the while loop w/o going further in this iteration.
        else:
            num_guesses += 1
            guess = int(guess)

        if guess < randNum:
            guess = input("Too low.  Guess again: ")
        elif guess > randNum:
            guess = input("Too high.  heh.  Guess again.")
        else:
            print("You got it in", num_guesses, "trys.")
            guessed_number = True

    print("Thanks for playing.")


main()


