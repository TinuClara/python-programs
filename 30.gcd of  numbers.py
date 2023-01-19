x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
i=1
while(i<x and i<y):
    if(x%i==0 and y%i==0):
        gcd=i
    i=i+1
print("gcd of ",x,"and",y," is ",gcd)