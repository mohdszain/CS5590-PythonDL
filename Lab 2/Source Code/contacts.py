from collections import defaultdict
def contacts():
    print("1. Contact By Name")
    print("2. Contact By Number")
    print("3. Edit Contacts By name")
    print("4. Exit")
    print()
contact_list =[{"Name":"Zain","Number":8167266155,"Email":"mohd.szain@gmail.com"},{"Name":"Aejaz","Number":8162178135,"Email":"aejaz@gmail.com"},{"Name":"Huaifa","Number":816420420,"Email":"autostar@gmail.com"}]
contacts()
menus = int(input("Enter a choice of yours between 1-4: ")) #The action to be performed is selected here
if menus == 1:
    Name = str(input("Please enter the contact name you wish to search:")) #Since the name is in string we are using Str before input
    for a in contact_list:
        if a["Name"] == Name: #If the name entered matches the name in the list it prints out the output
            print(a)
            break
        else:
            print("The name you entered not found in the directory")
            exit(0)

elif menus == 2:
    Number = int(input("Please enter the number to retreive contact details:"))
    for a in contact_list:
        if a["Number"] == Number: #It is the same thing as above since we are finding details through number
            print(a)
            break
        else:
            print("Check the number you have entered")
            exit(0)

elif menus == 3:
    Name = str(input("Please enter the contact name to update it's details:"))
    for a in contact_list:
        if a["Name"] == Name:
            print(a)
            Numb = int(input("Enter the new number:"))  #Since only the number may be changed we are just updating the number
            a["Number"] = Numb
            print("The updated details are:")
            print(a)
            break
        else:
            print("Please check the name you have entered")
            exit(0)
else:
    print("Thank you")
    exit(0)
