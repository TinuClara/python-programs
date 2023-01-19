#to check whether a number is prime or not

num=int(input("Enter the number: "))
i=2
count=0
while (i<num):
   if  num%i==0:
       count=count+1
   i = i + 1


if count==0:
    print("The number is prime")
else:
      print("The number is not prime")
