#number pattern
n=int(input("Enter the limit: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i*j,end=" ")
        j=j+1
    i=i+1
    print("\n")
