import random
print('How many pencils would you like to use:')

while True:
    pencils = input()
    if pencils.isnumeric() is False:
        print("The number of pencils should be numeric")
    elif int(pencils) < 0:
        print("The number of pencils should be numeric")
    elif int(pencils) == 0:
        print("The number of pencils should be positive")
    else:
        break

pencils = int(pencils)
print("Who will be the first (John, Jack):")

while True:
    name = str(input())
    if name != "John" and name != "Jack":
        print("Choose between John and Jack")
    else:
        break

print("|" * int(pencils))

while True:
    if name == "John":
        print("John's turn! ")

        while True:
            taken = input()
            if taken != "1" and taken != "2" and taken != "3":
                print("Possible values: '1', '2' or '3'")
            else:
                break

        taken = int(taken)
        print("|" * (int(pencils) - int(taken)))

        if taken < pencils:
            pencils -= taken
            name = "Jack"
        elif taken > pencils:
            print("Too many pencils were taken")
        elif taken == pencils:
            pencils -= taken
            if pencils == 0:
                print("Jack won!")
                break


    elif name == "Jack":
        print("Jack's turn: ")

        if pencils % 4 == 0:
            taken = 3
            print(taken)
            print("|" * (int(pencils) - int(taken)))
            pencils -= taken
            name = "John"

        elif pencils % 4 == 3:
            taken = 2
            print(taken)
            print("|" * (int(pencils) - int(taken)))
            pencils -= taken
            name = "John"

        elif pencils % 4 == 2:
            taken = 1
            print(taken)
            print("|" * (int(pencils) - int(taken)))
            pencils -= taken
            name = "John"

        elif pencils == 1:
            taken = 1
            print(taken)
            print("John won!")
            break

        else:
            taken = random.randint(1, 3)
            if taken > pencils:
                print("Too many pencils were taken")
            else:
                print(taken)
                print("|" * (int(pencils) - int(taken)))
                pencils -= taken
                name = "John"