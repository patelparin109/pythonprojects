x = 89
def parin():
    x = 20
    def keval():
        global x
        x = 66
    # print("Before calling keval()", x)
    keval()
    print("After calling keval()", x)
parin()
print(x)