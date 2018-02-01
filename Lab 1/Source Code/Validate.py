import re                                             #importing Regular expression for general expression patterns
def validation():                                      #defining a function
    while True:
        password = input("Enter a password for My UMKC : ")
        if len(password)< 6 or len(password) > 16:      #condition for length of the password
            print("Please enter a characters only between 6-16 ")
        elif re.search('[0-9]',password) is None:        #condition for validation number
            print("Please make sure your password contains atleast one number")
        elif re.search('[$@!*]',password) is None:      #condition for insertion for charaters
            print("Please make sure your password contains atleast one characters from [$@!*]")
        elif re.search('[a-z]', password) is None:      #lower case
            print("Please make sure your password contains atleast one lower case letter")
        elif re.search('[A-Z]',password) is None:       #upper case
            print("Please make sure your password contains atleast one upper case letter")
        else:
            print("Password accepted")
            break
validation()