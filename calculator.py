user_in=input('enter ur number')
oprator=['+','-','*',"/"]
for numbers in range(len(user_in)):
    if user_in[numbers] in oprator:   
        print(numbers,user_in[numbers])
        num1=int(user_in[:numbers])
        num2=int(user_in[numbers+1:])
        if user_in[numbers]=='+':
            print('sum is ',num1+num2)
        elif user_in[numbers]=='-':
            print('sub is ',num1-num2)
        elif user_in[numbers]=='*':
            print('mul is ',num1*num2)
        elif user_in[numbers]=='/':
            print('div is ',num1/num2)    
        


       