import random
import time 
def askname():

    user_name=input('please enter name>>>')
    db_feedback=[
    ]
    db=[
        {
            'greeting':[f'hi {user_name} what can i help u today ?  or Say (help)>>>>',f'hello Mr {user_name} ,what would u like to know about our School(say help)']
        },
        {
            'help':[f'okay {user_name} what would u like to know about \n 1.our  courses \n 2.course pricees \n 3.feedback'],
            'services':[f'currently we have 3 courses \n 1. python \n 2.react \n 3. js'],
            'course_price':[f'the react course cost u 1200$ \3 {user_name}',f'the js course cost u 1900$ \3 {user_name}',f'the python course cost u 1000$ \3 {user_name}']
        }
    ]
    def  main():
        while True:
            print(db[0]['greeting'][random.randint(0,1)])
            time.sleep(1)
            user_want=input('')
            time.sleep(1)
            if user_want=='help':
                print('*'*8)
                print(db[1]['help'][0])
                print('*'*8)

                services=input('please insert a number ')
                if services=='1':
                    time.sleep(1)
                    print(db[1]['services'][0])
                    ask=input('do u want to exit (Y/N)?? \n')
                    if ask=='y':
                        break
                    continue
                elif services=='2':
                    time.sleep(1)

                    what_sub=input('what course actually??\n')
                    if what_sub=='react':
                       time.sleep(1)
                       print(db[1]['course_price'][0])
                       ask=input('do u want to exit (Y/N) ??\n')
                       if ask=='y':
                        break

                       continue
                    elif what_sub=='js':
                       time.sleep(1)
                       print(db[1]['course_price'][1])
                       ask=input('do u want to exit (Y/N) ??\n')
                       if ask=='y':
                        break
                       continue
                    elif what_sub=='python':
                       time.sleep(1)
                       print(db[1]['course_price'][3])
                       ask=input('do u want to exit (Y/N) ??\n')
                       if ask=='y':
                        break
                       continue
                elif services=='3':
                   print('*'*12)
                   print('what do u want to say about our school (feedback)??')
                   feed=input('')
                   print(feed)
                   db_feedback.append(feed)
                   print(db_feedback)
    if user_name !='':
        main()
    else:
        print('please enter ur name firse ')
        askname()
askname()