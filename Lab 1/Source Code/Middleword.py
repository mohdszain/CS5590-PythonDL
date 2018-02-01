senten = input("Enter a sentence:")
def middle(x):
    a = senten.split()     #spliting the sentence into list
    length = len(a)
    if length % 2 == 1:     #checking whether the sentence has odd number words
         i = int(length/2)  # getting the postion of the middle word
         print("The middle word is :",a[i])        # printing the middle word
    else:                   #if the number of word are even
        i = int((length/2)-1)  #getting the postion of the middle two words
        j = int(length/2)
        print("the middle letters of the sentence are  :",a[i],a[j])       # print the middle two words since the sentence has even words
middle(senten)