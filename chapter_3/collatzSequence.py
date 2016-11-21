def collatz(number):
    if number % 2 == 0:
        tempNumber = number // 2
    else:
        tempNumber = 3 * number + 1

    print (str(tempNumber))
    return tempNumber


inputNumber = 0
collatzNumber = 0
try:
    print ("Please enter a number:  ", end = "")
    collatzNumber = int(input())

    while collatzNumber != 1:
        collatzNumber = collatz(collatzNumber)

except ValueError:
    print ("Please enter a valid number next time")
