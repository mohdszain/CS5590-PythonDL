senten = input("Enter a sentence:")
word_list = senten.split()       #spliting the sentence into list
def find_longest_word(word_list): #word_list is used to keep the list of the words
    word_len = [] #defining to keep the length of the words
    for n in word_list:
        word_len.append((len(n),n)) # appending the length of the word and the word
    word_len.sort()                 # sorting words according to length
    return word_len[-1][1]
print(find_longest_word(word_list))