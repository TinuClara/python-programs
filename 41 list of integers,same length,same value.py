x=[1,2,3,5,8]
y=[8,6,2,3]

if len(x)==len(y):
    print("Two lists are of equal length")
else:
    print("Two lists are of unequal length")
sum1=0
sum2=0
for i in range(0,len(x)):
    sum1=sum1+x[i]
for i in range(0,len(y)):
    sum2=sum2+y[i]
if sum1==sum2:
    print("Lists sums to equal values")
else:
    print("Lists sums to unequal value")


list=[]
print("The common elements in x and y are: ")
for i in x:
    for j in y:
        if i==j:
          print(i)



