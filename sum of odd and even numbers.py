sum =0
odd=0
num=int(input("Enter the number upto which the sum is to be finded"))
for i in range(1,num+1,1):
    if i%2==0:
        sum=sum+i
    else:
        odd=odd+i
print("Sum of even numbers is: ",sum)
print("Sum of odd numbers is: ",odd)

