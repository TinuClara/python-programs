#to check whether a number is armstrong or not

temp=0
num=int(input("Enter the number to check whether it is armstrong or not: "))
nnum=num
while (num>0):
    rem=num % 10
    temp=temp +rem * rem * rem
    num=num//10
print( temp)
if (temp == nnum):
    print("The number is armstrong")
else:
     print("The number is not armstrong")