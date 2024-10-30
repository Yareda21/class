# from classes import *     # everything

def registration():
    name = input("Enter your name:_")
    age = int(input("Enter ur age"))


    customer = BOA(name,age)

    database.append(customer)
    print("Regs succes")


# def withdraw(customer):
#     money = int(input("Enter amount: "))

#     if money >= customer.get_balance():
#         print("Not enough money!!")
#     else:
#         currentBalance = customer.get_balance() - money
#         customer.set_balance(currentBalance)
#         print("Withdraw successfull! \nCurrent balance ", customer.get_balance() )


# def transfer(customer):
#     counter = 0
#     while counter + 3:
#         transfer = int(input("how much amount to transfer:_"))
#         if transfer >= customer.get_balance():
#             print("money not enough")
#             counter =+1

#         else:
#             counter = 0
#             while counter < 3:
#                 other_account = int(input("Enter the other person account:_"))
#                 data = [account for account in database if account.get_account() == other_account]

#                 if (len(data) == 0):
#                     print("Account unavailable!!")
#                     continue
#                 else:
#                     customer2 = data[0]
#                     transfer_money = int(input("Enter Amount to transfer: "))
#                     if customer.get_balance() < transfer_money:
#                         print("Insufficient balance!")
#                         counter += 1
#                         if (counter == 3):
#                             exit()
#                         continue
#                     else:
#                         newBalance1 = customer.get_balance() - transfer_money
#                         customer.set_balance(newBalance1)
#                         print("Curent balance for cus 1: ", customer.get_balance())
#                         newBalance2 = customer2.get_balance() + transfer_money
#                         customer2.set_balance(newBalance2)
#                         print("Customer 2 current balance: ", customer2.get_balance())
#                         break



# def deposite(customer):
#     counter = 0
#     while counter + 3:
#         accontNO = int(input ("Enter your account number:_"))
#         if accontNO != customer.get_account():
#             counter =+1
#             print("anaviable account")
#             quit()
#         else:
#             amountM = int(input("enter the amount you would to like to deposite to_:"))
#             customer.get_newbalance() + amountM 
#             print("your balance is " ,customer.set_newbalance())
        
from classes import *



customer = int(input("Enter your choice:_"))

def withdraw (customer):
    money = int(input("Enter the amount to withdraw:_ "))
    account = int(input("Enter your account number:_"))
    
    if money >= customer.get_account():
            print("insuffecient fud")
        
    else:
        currentbalance = customer.get_balance() - money
        customer.set_balance =(currentbalance)
        print("your amount is", currentbalance)

def transfer(customer):
    counter = 0
    while counter + 3:
            transfer = int(input("Enter the amount to transfer:_"))
            if transfer >= customer.get_account():
                print("Money not enough")
                counter =+ 1
            else:
                counter = 0
                account2 = int(input("enter the another account:_"))
                data = [ account for account in database if account.get_account() == account2 ]
                if (len(data = 0)):
                    print("anavialable account")
                    counter =+ 1
                    if( counter == 3):
                        exit()
                    continue
                else:
                    counter = 0
                    while counter < 3:
                         account2(0)
                         transfer = int(input("enter the amount:_"))
                         if transfer >= customer.get_account():
                          print("insufficient amount")
                         counter =+ 1
                         if ( counter == 3):
                                exit()
                    else:       
                        currentbalance = customer.get_account() - transfer
                        customer.set_account(currentbalance)
                        print("transfer successfull \ncurrent amount" , currentbalance)


def deposit(customer):
        accountNO = int(input("enter account number:_"))
        if accountNO != customer.get_account:
            print("wrong account number")
        else:
            money = int(input("Enter the anount:_"))
            customer.set_account() == customer.get_account() + money 
            print ("your amount is ", customer.get_account())     
                        
                    
