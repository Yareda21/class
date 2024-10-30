import random
def dice_game(gamer):

    number = random.randint(1,14)
    

    if gamer == number:
        return ("You won the bet")
        

    elif gamer != number:
        return ("U lost the bet")           
 

    
    elif gamer == "yes":
        return