f = open("parin.txt","rt")
print(f.readlines()) # read in list

print(f.readline())
print(f.readline())
print(f.readline())

content = f.read()

for line in f:
    print(line, end=" ")

content = f.read(344)
print("1",content)

content = f.read(344)
print("2",content)

f.close()