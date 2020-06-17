# Health Management System
# 3 clients - Parin Keval and Bunty

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# Write a function that when executed takes as input client name.
# One more function to retrieve exercise or food for any client.

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if(k==1):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            value = input("Type Here\n")
            with open("parin-ex.txt","a") as op:
                op.write(str([str(gettime())])+" : "+value+"\n")
            print("Successfully Written")
        elif(c==2):
            value = input("Type Here\n")
            with open("parin-food.txt","a") as op:
                op.write(str([str(gettime())]) + ":" +value+ "\n")
            print("Successfully Written")
    elif(k==2):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if(c == 1):
            value = input("Type Here\n")
            with open("keval-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written")
        elif(c == 2):
            value = input("Type Here\n")
            with open("keval-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("Successfully Written")
    elif(k==3):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("Type Here\n")
            with open("bunty-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written")
        elif (c == 2):
            value = input("Type Here\n")
            with open("bunty-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("Successfully Written")
    else:
        print("plz enter valid input (1(parin),2(keval),3(bunty)")

def retrieve(k):
    if (k==1):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("parin-ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif(c==2):
            with open("parin-food.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif(k==2):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("keval-ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("keval-food.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif(k==3):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("bunty-ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("bunty-food.txt") as op:
                for i in op:
                    print(i, end=" ")
    else:
        print("plz enter valid input (parin,keval,bunty)")
print("Health Management System: ")
a = int(input("Press 1 for log the value and 2 for retrieve"))

if a == 1:
    b = int(input("Press 1 for Parin 2 for Keval 3 for Bunty"))
    take(b)
else:
    b = int(input("Press 1 for Parin 2 for Keval 3 for Bunty"))
    retrieve(b)







