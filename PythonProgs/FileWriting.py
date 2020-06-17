# f = open("parin.txt","w")
# a = f.write("Parin is very Cleaver...")
# print(a)
# f.close()

# handle read and write both

f = open("parin.txt","r+")
print(f.read())
f.write("Thank You")