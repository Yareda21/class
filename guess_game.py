import random
import time
db=[]

while True:
   bet=float(input('enter ur batting money>>>>'))
   time.sleep(0.5)
   ask=int(input('enter ur guess>>>>>>>'))
   time.sleep(0.5)

   comuter_g=random.randint(0,9) 
   time.sleep(0.5)
   bet_plus=30
   bet_plus+=bet#bonus amount 30$
   if (bet<10):
                time.sleep(0.5)

                print('please increase ur betting buget it must be 10 or above ') 
                print('*'*10)
                break
   if(ask =='' or bet ==''):
         continue
   time.sleep(0.5)

   print(f'computer guess is {comuter_g}')
   print('*'*10)

   time.sleep(0.5)

        
   print('u r betting by this money ',bet_plus)
   time.sleep(0.5)
   if (comuter_g>ask):
            print('******above ur guess*********')
   elif(comuter_g<ask):

            print('********below ur guess ********** ')
   elif(comuter_g==ask):
         print('u got it  ')
   if (comuter_g>ask or comuter_g <ask):
                print(f'u lose \n ur current amount is {bet_plus-10}')
                x="lose"
   elif(comuter_g==ask):
                print(f'u won ur current balance is {bet_plus+10}')
                x='win'
      
   betting={ 
            'time u bet ':time.ctime(),
            'ur betting money ':bet_plus,
            'lose/win':f"{x}",
         }
   db.append(betting)
   print('*'*10)

   br_=input('do u want to bet again   >>>>')
   if (br_=='n'):
                break
for everyBet in db:
      print(everyBet)
