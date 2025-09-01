l=['a','e','i','o','u']
str=input("Enter a string: ")
vc=0
cc=0
for char in str:
    if char in l:
        vc+=1
    else:
        cc+=1
print("No. of vowels =",vc)
print("No. of consonents =",cc)