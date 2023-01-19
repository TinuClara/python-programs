#sum of odd and even numbers using while loop

num=int(input("Enter limit: "))
n=1
even=0
odd=0
while(n<num):
    if(n%2==0):
      even=even+n

    else:
      odd=odd+n
    n=n+1
print("Sum of even numbers is ",even)
print("Sum of odd numbers is ",odd)