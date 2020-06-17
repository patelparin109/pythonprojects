# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Parin", "Keval", "Jay", "Priyank", "Priya")

pal = ["Parin", "Keval", "Jay", "Priyank", "Priya", "The programmer"]
normal = "I am a normal Argument and the students are:"
kev = {"Keval":"Monitor", "Parin":"Fitness Instructor",
      "The Programmer": "Coordinator", "Jay":"Cook"}
funargs(normal, *pal, **kev)