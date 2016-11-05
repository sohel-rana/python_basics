# a divide function, will try to divide by 0
def divide(divisor, denominator):
    try:
        return divisor/denominator
    except ZeroDivisionError:
        print ("You tried divide by zero")

print (divide(100, 10))
print (divide(100, 0))
print (divide(200, 5))

# try to open a file which don't exist
try:
    open("hello.txt", mode='r')
except IOError:
    print ("No file found")
