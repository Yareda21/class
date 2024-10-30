from calculator import calculator
from chat_bot import chatbot
from dice_rolling import dice_game
from guess_game import guess_game
from temp_converter import temp_converter
from word_counter import word_counter
from classes import bank
import random

print("Yoram")


if __name__ == "__main__":
    while True:
        print("My App..")
        print(
            "1.calculator \n"
            "2.dice game \n"
            "3.chat bot \n"
            "4.Guess game \n"
            "5. temperature converter \n"
            "6. word counter \n"
            "7. bank"
            )
        user = int(input("Enter your choice:_"))
        if user == 1:
            while True:
                n1 = int( input("enter num : _"))
                op = input("enter your symbol: _")
                n2 = int(input("enter your num:_"))
                answer = calculator(num1=n1, opr=op, num2=n2)
                print(answer)
                continue
        elif user == 2:
            
            while True:
                gamer = int(input("Enter the number your betting on:_"))
                answer = dice_game(gamer=gamer)
                print(answer)
                ask = input("Do you want to continue:_")
                    
                if ask == "no":
                    break 
                        
        elif user == 3:
    
            while True:
                greeting = {
                "hi": [ "heyy" , "hello there"] ,
                "how are you": ["I am fine " , " doing good"],
                "what is your name" :["my name is Dello" , " you can call me Ahmed"],
                "what country is the best for studying I.T": ["America", "Spain", "UAE" ,"Ehtopia","any but not in africa"],
                "thanks":[ "welcome", "Anytime"]
            }
                talk = input(" : ")
                answer = chatbot( talk ,greeting)
                print(answer)
                
                
        elif user == 4:
            while True:
                number = random.randint(1 , 100)
                while True:
                    guess = int(input("enter your guess: _"))
                    answer = guess_game(guess, number)
                    print(answer)
                    if answer == "You guess correct":
                        break
                    

                
                ask = input("Do you want to countine:_")
                if ask == "no":
                    break
                elif ask == "yes":
                    continue    


        elif user == 5:
            while True:
            
                custemer = input("Enter your unit f or c:_")
                temp = int(input("enter the number:_"))
                answer = temp_converter(custemer, temp)

                print(answer)
                ask = input("Do you want continue:_")
                if ask == "yes":
                    continue
                elif ask == "no":
                    break

        
        elif user == 6:
            while True:
                user = input("Heollo tell me about your day: _")
                answer = word_counter(user)
                print(answer)
                ask = input ("Do want to continue:_")
                if ask == "yes":
                    continue
                if ask == "no":
                    break
        
        elif user == 7:

        else: 
            print("Unaviable choice")
        continue
        
        


