#reverse of a number

temp=0
num=int(input("Enter the number to be reversed: "))
while (num>0):
    rem=num % 10
    temp=temp*10 +rem
    num=num//10
print( "Reverse of the given number is ",temp)
