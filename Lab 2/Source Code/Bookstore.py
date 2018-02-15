fiction = {'Nancy drew':20,'Harry Potter':40,'Ready Player one':10,'Call me by your name':30}
print("Enter a range for books to purchase")
x = int(input("Starting value:"))
y = int(input("Ending value:"))
print("The books purchsed are:")
for key in fiction:
    if fiction[key]>=x and fiction[key]<=y :
        print(key)

