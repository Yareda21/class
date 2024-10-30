def word_counter(user ):
    counter = 0
    for x in user:
        if x == " ":
         counter += 1
    return("Number of words:", counter)

