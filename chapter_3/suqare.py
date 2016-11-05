
def square(numberParam):
    return numberParam * numberParam

print("***** This program finds the square of the number you put. Please enter a number : ")
number = input()
squareTotal = square(int(number))
print ("Square of " + number + " is : " + str(squareTotal))