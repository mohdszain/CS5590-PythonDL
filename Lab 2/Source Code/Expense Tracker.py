print(" Welcome to Budget Tracker application \n Please provide your details:")
name = input("Enter your name:")
age = int(input("Enter your age:"))
number = int(input("Enter your contact number:"))
email = input("Enter your email address:")
ssn = int(input("Enter your SSN:"))
limit = int(input("How much amount do you wish to track:"))

#__init__ constructor and self are implemented in every class.
#creating class 1
class Details():
    def __init__(self,name,age,email,number):
        self.name = name
        self.age = age
        self.email = email
        self.num = number

    def details(self,sa):
        self.__ssn = sa        #Making SSN as a private variable
        print("\n Name of the person: ", self.name + "\n Email address: ", self.email,"\n Age:",self.age,"\nContact number:", self.num,"\nSocialsecurity number:", self.__ssn)

#defining class 2 from class 1
#Inheriting classes and implementing super in this class
class Income(Details):
    income = 0

    def __init__(self, name, age, email, number):
        # super is implemented here
        super(Income, self).__init__(name, age, email, number)

    def update_salary(self):
        self.a = int(input("Enter your savings"))
        self.__class__.income = self.__class__.income + self.a
        print("Total savings: ", self.__class__.income)
#definig class 3 from class 1
# Ineritance implemented
class Addexpense(Details):
    a = 0

    def __init__(self, name, age, email, number):
        Details.__init__(self, name, age, email, number)

    def update_expense(self):
        b = []
        c = int(input("Enter the number of expenses you want to add:"))
        for x in range(0, c):
            t = int(input("Add your expense here "))
            b.append(t)
        print("List of expenses added", b)
        self.exp = sum(b)
        self.__class__.a = self.__class__.a + self.exp
        print("Sum of expenses added:", self.__class__.a)

#definin class 4 from class 2 and class 3
class Balance(Addexpense, Income):  #multiple Inheritance implemented
    bal = 0
    def __init__(self):
        print("Check your balance here:")
    def balance(self):
        self.__class__.bal = Income.income - Addexpense.a
        print("Total Savings:",Income.income)
        print("Total Expenses:", Addexpense.a)
        print("Amount Left:", self.__class__.bal)

#defining class 5 from class 4
class Tracking(Balance):
    def __init__(self, l):
        self.tr = l
        if (Balance.bal < self.tr):
            print("Your remaining balance:",Balance.bal)
            print("Your balance is less than your set limit")
        elif (Balance.bal > self.tr):
            print("Your remaining balance:", Balance.bal)

u = Details(name, age, email, number)
u.details(ssn)
v = Income(name, age, email, number)#Here Instance of a class Income 'v' is created and it extends instance of the class Details 'u'
v.update_salary()  #updating the salary of instance 'v'
w = Addexpense(name, age, email, number)  #Here the Instance of class Addexpense 'w' is created and it extends instance of the class Details 'u'
w.update_expense()  #updating the expenses of instance 'w'
x = Balance() #Here Instance of class Balance 'x' is created and it extends instance of classes Income 'v' and Addexpense 'w'
x.balance()  #Here we are checking balancing with the instance 'w'
y = Tracking(limit) #Here the Instance of class Tracking 'y' is created and it extends instance of the class Balance 'x'
v.update_salary()
w.update_expense()
x.balance()
y.__init__(limit)