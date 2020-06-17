l = 10    # Global Variable

def function1(n):
    # l = 5  # Local Variable
    m = 7  # Local Variable
    global l
    l = l + 6
    print(l,m)
    print(n,"I have printed")

function1("This is me")
print(l)
