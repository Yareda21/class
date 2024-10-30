import random 



def guess_game(guess, number):
    
   
    print(number)
    if number == guess:
        return("You guess correct")
    elif number < guess:
       
        return("Guess lower:")
    elif number > guess:
    
        return("Guess higher:")   


