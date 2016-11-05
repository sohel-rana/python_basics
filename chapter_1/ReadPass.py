passwordFile = open("pass.txt");
secretPassword = passwordFile.read();

print ("Enter your password");
typedPassword = input();

if typedPassword == secretPassword:
    print ("Access granted.")
    if typedPassword == "123456":
        print ("Don't be an idiot. Choose password carefully")

else :
    print ("Password mismatch. try again later!")