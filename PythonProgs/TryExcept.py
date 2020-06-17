print("Enter Number 1 : ")
num1 = int(input())
print("Enter Number 2 : ")
num2 = int(input())
try:
    print("The sum of these two number is : ",
        int(num1) + int(num2))
except Exception as e:
    print(e)
print("Thia line is very important")