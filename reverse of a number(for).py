temp=0
num=int(input("Enter the number to be reversed: "))
for i in range(num):
    if num>0:
       rem=num % 10
       temp=temp*10 +rem
       num=num//10
    else:
        num<0
        break

print( "Reverse of the given number is ",temp)
