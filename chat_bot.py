def chatbot(talk , greeting):
    import random
    counter = 0
    while counter < 5:
        
        
        if talk == "hi":
            rand = random.randint(0,1)
            return(greeting ["hi"][rand])
            counter + 1   
        elif talk == "what is your name":
            rand = random.randint(0,1)
            return(greeting["what is your name"][rand])
            counter + 2
        elif talk == "how are you":
            rand = random.randint(0,1)
            return(greeting["how are you"][rand])
            counter + 3
        elif talk == "what country is the best for studying I.T":
            rand = random.randint(0,4)
            return(greeting["what country is the best for studying I.T"][rand])
            counter + 4 
        elif talk == "thanks":
            rand = random.randint(0,1)
            return(greeting["thanks"][rand])
            
        