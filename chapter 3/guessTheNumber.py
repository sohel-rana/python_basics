
import random

print ("I am thinking of a number between 1 and 20.")

numberPicked = random.randrange(1, 20)
countGuess = 0
userNumber = 0

while numberPicked != userNumber:
    countGuess += 1
    print ("Take a guess : ", end="")
    userNumber = int(input())
    if userNumber == numberPicked:
        print ("Good Job! You guessed my number in " + str(countGuess) + " guesses")
    elif countGuess == 10:
        print ("Too many attempts. Better luck next time. The number was " + str(numberPicked))
        break
    elif userNumber < numberPicked:
        print ("The guess is too low! Try again")
    elif userNumber > numberPicked:
        print ("The is too high! Try again")

