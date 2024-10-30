# to class from another file
from classes import BOA
# to do crud operation- create, read, update, delete
from classes import database
from modules import *

# to Start the application
if __name__ == "__main__":
  # to keep on running
    while True:
      # to show on the display - Welcoming the user
        print("welcome to BOA")
        # to identify the person
        account_input = int (input ("enter your account:_"))

        # checking the info from the database 
        data = [ account for account in database if account_input == account.get_account()  ]

        
        if (len(data) == 0):
            print("Unavailable")
            registration()
            continue
        else:
            customer = data[0]
            print("Hey", customer.get_name())
            # to make sure the user 
            counter = 0
            while counter < 3:
              password_input = int(input("Enter pin: "))
          
              if (customer.get_pin() != password_input ):
                print ("Wrong pin") 
                counter+=1
                if counter == 3:
                   exit()
                continue
              else:
                 break

            print("what do u like to do? \n"
                "1. To withdraw \n"
                "2. to transfer \n"
                "3. deposit \n" 
              )
            ask = int(input("enter your choice:_"))
            if ask == 1:
              withdraw(customer)
              continue
            elif ask == 2:
              transfer(customer)
            elif ask == 3:
              deposit(customer)
            else:  
                continue           




#         data = [ask1 for name in database if ask == name.get_name()]
        
#         data = [ask2 for pin in database if ask2 == pin.get_pin()]
#         # to match the data n show us
#         print (data)
#         # what to if the input doesnt match the data
#         if ask != data and ask1 != database.get_name and ask2 != database.gat_pin :
#           # show us wat if the doesnt match the database 
#           print("Wrong account number & wrong name")
#           # to keep us on the lopp
#           continue
        



# # from classes import BOA
# # from classes import database

# # if __name__ == "__main__":
# #     print("Welcome to boa")
# #     ask = input("enter your name:_")
# #     ask1 = int(input("enter your account:_"))
# #     data =[ask for name in database]
# #     if ask1 == get.account():
# #         print(data)
# #     if ask == name.get_name():
# #         print (data)


















