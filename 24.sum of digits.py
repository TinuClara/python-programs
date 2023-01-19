#sum of digits


temp=0
num=int(input("Enter the number whose sum of digits is to be finded: "))
while (num>0):
    rem=num % 10
    temp=temp +rem
    num=num//10
print("Sum of the digits",temp)