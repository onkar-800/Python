#Genetare a random number and make user to guess it 
#Give user instruction to Enter higher or lower number
from random import randint
def playgame():
    guess = randint(1,100)
    guesses = 0
    while True:
        guesses += 1
        user = int(input("Enter a number to guess: "))
        if user == guess:
            print("Congrats your guess is right")
            print(f"You guess a number in {guesses} guesses")
            return
        elif user < guess:
            print("Enter a higher number")
        else:
            print("Enter a lower number")


if __name__ == '__main__':  
    playgame()
    