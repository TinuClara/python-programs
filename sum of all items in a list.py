#sum of all items in a list
sum=0
list=[]
x=int(input("Enter the size of the list: "))
print("Enter the elements:")
for i in range(x):
    y=int(input())
    list.append(y)
print("List: ",list)
for i in range(x):
    sum=sum+list[i]
print("sum of elements in the list is: ",sum)
