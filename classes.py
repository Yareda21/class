class BOA:
    def __init__(self,name, age , id , gender , balance , account , pin ) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.gender = gender
        self.balance = balance
        self.account = account
        self.pin = pin


    # getters and setters 
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age



    def set_name(self, newName):
        self.name = newName

    def get_id(self):
        return self.id 
    def set_id(self,newid):
        self.id = newid

    def get_gender(self):
        return self.gender
    def set_gender(self, newgender):
        self.gender = newgender
    
    def get_balance(self):
        return self.balance
    def set_balance(self , newbalance):
        self.balance = newbalance
    
    def get_account(self):
        return self.account
    def set_account(self, newaccount):
        self.account= newaccount
    
    def get_pin(self):
        return self.pin
    def set_pin(self, newpin):
        self.pin = newpin




database = []

yoram = BOA("Yoram", 23, 1234, "Male", 1234, 1234, 1234)
sem = BOA("Sem", 21, 4321, "Male", 4321, 4321, 4321)
database.append(yoram)
database.append(sem)


