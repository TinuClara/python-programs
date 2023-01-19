n=int(input("Enter number of rows: "))
i=1
while (i<=n):
    j=1
    while (j<=i):
        print("*",end=" ")
        j=j+1
    i=i+1
    print("\n")
i=1
while (i<=n):
    j=n-1
    while (j>=i):
        print("*",end=" ")
        j=j-1
    i =i+1
    print("\n")


