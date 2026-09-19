class Account:

#constructor
    def __init__(self,accountNumber,name,age,balance,accountType,status):
        self._accountNumber = int(accountNumber)
        self._name =str(name)
        self._age = int(age)
        self._balance = float(balance)
        self._accountType__ = str(accountType)
        self._status = "Active"

#Method
def deposit(self,amount):
    if amount >0 :
        self._balance += amount 
        return True
    return False


def withdraw(self,amount):
    if amount>0:
        if self._balance >=amount:
            self._balance -=amount
            return True
    return False

def getAccountNumber(self):
    return self._accountNumber

def getName(self):
    return self._name

def getAge(self):
    return self._age

def getBalance(self):
    return self._balance

def getAccountType(self):
    return self._accountType

def getStatus(self):
    return self._status

def setName(self, name):
    self._name = str(name)

def setAge(self,age):
    self._age - int(age)







     
        