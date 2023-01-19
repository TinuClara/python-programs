#fibonacci series

a=0
b=1
i=0
num=int(input("enter the limit: "))
print(0,end=" ")
while(i<=num):
    c =a + b
    a=b
    b=c
    print(c,end=" ")
    i=i+1

