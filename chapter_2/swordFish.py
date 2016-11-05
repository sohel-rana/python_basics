while True:
    print ("Enter your name")
    name = input()
    if name != "sohel":
        continue
    print ("Welcome " + name + ". What is the password?")

    password = input()
    if password == "hilsha":
        break

print ("Access granted! Your choice of password is awesome!")

