# student 
#  emoloyee
# bank customer 


class Student:
    def __init__(self, fname, lname, pnumber, coursename, schadule, time):
        self.fname = fname
        self.lname = lname
        self.pnumber = pnumber
        self.coursename = coursename
        self.schadule = schadule
        self.time = time


student1 = Student("etse", "ketsela"," +2519111111", "pyton", "monday_wensday_friday", 3_5)
print(student1.coursename)
print(student1.fname)


class Employee:
    def __init__(self, fname, lname, phnumber, addresse, acadamic_status, position):
        self.fname = fname
        self.lname = lname
        self.phnumber = phnumber
        self.addresse = addresse
        self.status = acadamic_status
        self.position = position

    
employee1 = Employee("eden", "siyuom", 25191222222, "addis", "degree", "accountatn")
print(employee1.addresse)
print(employee1.phnumber)
        


class Bank_customer:
    def __init__(self, fname, lname, account_number, money_deposit, date, signituer):
        self.fname = fname
        self.lname = lname
        self.account_number = account_number
        self.money_deposit = money_deposit
        self.date = date
        self.signituer = signituer

    def withdraw(self,money):
        print(self.fname,"is limited to withdraw", money)


        
customer1 =Bank_customer("ayele", "tasie", "10001820278", 2570, "8/7/2020", "yyyy")
print(customer1.account_number)
print(customer1.withdraw(50000))

   

    
        

    