# to check whether a number is paliandrome or not

temp=0
num=int(input("Enter a number to check whether it is pliandrome or not: "))
nnum=num
while (num>0):
    rem=num % 10
    temp=temp*10 +rem
    num=num//10
print( temp)
if (temp == nnum):
    print("The number is paliandrome")
else:
     print("The number is not paliandrome")