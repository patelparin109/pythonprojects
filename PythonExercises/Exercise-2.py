# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

#45*3=555 #56+9 = 77 #56/6 =4

first_number = int(input("1st number"))
second_number = int(input("2nd number"))
operator = (input("choose operator"))
if first_number == 45 and second_number == 3 and operator == "*":
    print("555")
elif first_number == 56 and second_number == 9 and operator == "+":
    print("77")
elif first_number == 56 and second_number == 6 and operator == "/":
    print("4")
else:
    if operator == "+":
        print(first_number + second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    elif operator == "-":
        print(first_number - second_number)
