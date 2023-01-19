#fibonacci series


a=0
i=0
num=int(input("enter the limit: "))
for i in range(0,num+1):
    c = a + i
    a=i
    i=c
    print(c,end=" ")
