
from datetime import datetime

currentHour = datetime.now().strftime('%H')
currentTime = datetime.now().strftime('%H:%M:%S')
print ('It is ' + currentTime)

currentHour = int(currentHour)

quitChar = 'Q'

if currentHour < 6:
    print ("Man! you need some sleep. Try sometimes later. Press Q to quit, any other character to continue")
    quitInput = input()
    if quitInput == quitChar:
        exit(0)
elif currentHour > 19:
    print ("Good Night! See you in the morning. Press Q to quit, any other character to continue")
    quitInput = input()
    if quitInput == quitChar:
        exit(0)

elif currentHour > 12:
    print ("Good Afternoon!")
else:
    print ("Good Morning!")


print ("What is your name?")
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is ", str(len(myName)))

print("What is your age?")
myAge = input()

print('You will be ' + str(int(myAge) + 2) + "after 2 years")


