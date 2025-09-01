a=int(input())
temp=a
temp2=a
n=0
while(temp):
    n+=1
    temp=temp//10
# print(n)
sum=0
while(a):
    rem=a%10
    sum=sum+(rem**n)
    a=a//10
print(sum)
if(temp2==sum):
    print("Armstrong number")
else:
    print("Not armstrong number")