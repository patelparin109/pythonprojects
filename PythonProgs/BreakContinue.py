i = 0

while(True):
    if i + 1 < 5:
        i = i + 1
        continue
    print(i+1, end =" ")
    if (i == 44):
        break # stop the loop
    i = i + 1



while(True):
    inp = int(input("enter a number"))
    if inp > 100:
        print("Number is greater than 100")
        break
    else:
        print("Try Again!")
        continue
