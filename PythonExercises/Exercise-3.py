n = 18

number_of_guesses = 1
print("Number og guesses is limited to only 9 times:")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number : \n"))
    if guess_number < 18:
        print("You enter less number please input greater number. \n")
    elif guess_number > 18:
        print("You enter greater number please input smaller number \n")
    else:
        print("You Won!!! \n")
        print(number_of_guesses,"No. of guesses left")
        break
    print(9- number_of_guesses, "No. of guesses left...")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses)>9:
    print("Game Over!!!!!")



