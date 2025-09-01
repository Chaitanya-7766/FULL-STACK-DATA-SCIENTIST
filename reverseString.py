str=input("Enter any string:\n")
print("The string is: ",str)
rev=""
for char in str:
    rev=char+rev
print("The reverse of the string is: ",rev)