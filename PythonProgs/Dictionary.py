# Dictionary in Python:

dict = {"Parin":"Burger",
        "Kiran":"Samosa",
        "Keval":{"Breakfast":"Tea","Lunch":"Pulav","Dinner":"Pizza"}}

print(dict)

print(dict["Parin"])
print(dict["Keval"]["Dinner"])
dict["Mayur"] = "Junk Food"

print(dict)

dict[420] = "Pav Bhaji"

print(dict)

del dict[420]
print(dict)

dict2 = dict

del dict2["Mayur"]

print(dict.copy())

print(dict2.update({"Leena":"Chole Bhature"}))
print(dict2)


print(dict2.keys())
print(dict2.items())


