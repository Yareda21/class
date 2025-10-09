operators = ["+", "-", "*", "/"]

# num1, opera, num2
# def calculator(expression):
#     for index in range(len(expression)):
#         if expression[index] in operators:
#             oper = expression[index]
#             num1 = int(expression[0:index])
#             num2 = int(expression[index+1:])

#     if oper == "+":
#         return num1 + num2
#     elif oper == "-":
#         return num1 + num2
#     elif oper == "*":
#         return num1 + num2
#     elif oper == "/":
#             return num1 / num2
    
    


#num1, oprato, num2

def calculator(expression):
    for index in range(len(expression)):
        if expression[index] in operators:
            oper = expression[index]
            num1 = int(expression[0:index])
            num2 = int(expression[index+1:])
            


    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        return num1 / num2

        
            
            




    
    
    
    
    
    



