senten = input("Enter a sentence:")
def reverse():
    a = senten[::-1] #reversing the given string and storing in different variable
    b = a.split() #spliting the sentence into list
    print(' '.join(reversed(b))) #reversed function used to reverse the string
reverse()