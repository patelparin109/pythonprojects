
import os
print(dir(os))
print(os.getcwd())
os.chdir("C://")
print(os.getcwd())
f = open("parin.txt")
print(os.listdir("C://"))
os.makedirs("This/that")
os.rename("parin.txt", "parin-ex.txt")
print(os.environ.get('Path'))
print(os.path.join("C:/", "/parin.txt"))

print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))
