list1 = ["Parin","Keval","Bunty","Jay"]
tuple = ("Parin","Keval","Bunty","Jay")

list2 = [["Parin",1],["Keval",3],["Bunty",6],["Jay",9]]
dict1 = dict(list2)

for item in list1:
    print(item)

for item in tuple:
    print(item)

for item, lollypop in list2:
    print(item, "and lollypop is", lollypop)

for item, lollypop in dict1.items():
    print(item, "and lollypop is", lollypop)

for item in dict1:
    print(item)

items = [int,float, "Parin",5,6,7,3,4,8,22,33,45,34,34,666]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)
