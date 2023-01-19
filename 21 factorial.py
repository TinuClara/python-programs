#to find factorial of a number

fact=1
i=1
num=int(input("Enter the number whose factorial is to be finded: "))
while(i<=num):
    fact=fact * i
    i=i+1
print("Factorial of",num,"is",fact)