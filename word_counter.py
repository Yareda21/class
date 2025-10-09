# text = input("Enter Text: ")


def wordCounter(file_name):
    with open(file_name) as file:
        data = file.read()
        # print(data)
        counter = 0
        for leter in data:
            if leter == " ":
                counter = counter + 1
        
        return counter

