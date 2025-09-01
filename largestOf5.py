str=input("Enter ',' separated 5 integers")
l=[int(x) for x in str.split(",")]
print(l)
max=l[0]
for i in range(1,5):
    if l[i]>max:
        max=l[i]
print("The maximum in the list is: ",max)
