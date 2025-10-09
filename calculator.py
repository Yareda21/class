num = input('Enter numbers:\n')
opperations = ["+","-","*","/"]

for index in range(len(num)):
    if num[index] in opperations:

        opp_1 = num[index]
        num_1 = int(num[0:index])
        num_2 = int(num[index+1:])
        
        if opp_1 == '+':
            print("Ans:", num_1 + num_2)     
        elif opp_1 == "-":
            print("Ans:", num_1 - num_2)
        elif opp_1 == "*":
            print("Ans:", num_1 * num_2)
        elif opp_1 == "/":
            print("Ans:", num_1 / num_2)