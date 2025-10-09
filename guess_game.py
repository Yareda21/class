import random 
computer_number = random.randint(0,100)

guess = int(input("Enter your guess: "))

if computer_number == guess:
    print("Correct guess!!")
elif computer_number > guess:
    print("Wrong! Try Guessing higher")
elif computer_number < guess:
    print("Wrong! Try Guessing lower")
else:
    print("Wrong input!!")


