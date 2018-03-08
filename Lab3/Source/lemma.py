import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize,sent_tokenize
from collections import Counter
from nltk.util import ngrams

#Reading the file
text = (open('samp.txt').read())
#print(text)
#Sentence tokeniztion
senten = sent_tokenize(text)

#Word Tokenization
wordtoken = []
for alpha in senten:
    wordtoken.append(word_tokenize(text))
print("Tokeniztion:")
print(wordtoken)

#Lemmatization
lemdata = []
lema = WordNetLemmatizer()
for lem in wordtoken:
    for word in lem:
        lemdata.append(lema.lemmatize(word))
print("Lemmatization")
print(lemdata)

#bigram
nword = nltk.word_tokenize(text)
bigram = list((ngrams(nword,2)))
print("Printing bigrams")
print((bigram))

grams = Counter(ngrams(nword,2))
tem = []
tem = grams.most_common(5)

#print top 5 bigrams
print("Top 5 bigrams that has been repeated most:",tem)

bucket = []
for word in tem:
    bucket.append(word[0])   #Picking the top 5 repeated strings.
s=[]

for single_line in text.splitlines():
    for a in range(5):
        if bucket[a][0] in single_line.split() and bucket[a][1] in single_line.split():
            s.append(single_line)
print(s)