
myCats = []
print("******Enter your cat name or enter nothing to stop.*****")

while True:
    print ("Enter the name of your " + str(len(myCats) + 1) + " number cat : ", end = '')
    name = input()
    if name == '':
        break

    myCats = myCats + [name]

print ("Your cat names are :")
for name in myCats:
    print (name)