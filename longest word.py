a=[]
n=int(input("Enter the no. of words:"))
print("enter words:")
for i in range(0,n):
    value=input()
    a.append(value)
max=len(a[0])
temp=a[0]
for i in a:
    if len(i)>max:
        max=len(i)
        temp=i

print("longest word is ",temp)
print("longest word length is ",max)

