import numpy as x      #Using numpy Library
Y = x.random.randint(0,20,size=15)    #Creating a Vector list of 15 random numbers
print(Y)
print("The most common integer in the list is:",x.bincount(Y).argmax())