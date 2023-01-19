#to find factorial of a number

fact=1

num=int(input("Enter the number whose factorial is to be finded: "))
for i in range(1,num+1):
    fact=fact * i
print("Factorial of",num,"is",fact)