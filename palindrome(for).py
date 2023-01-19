# to check whether a number is paliandrome or not

temp=0
nnum=int(input("Enter a number to check whether it is pliandrome or not: "))
num=nnum
for i in range(nnum):
      if nnum > 0:
         rem=nnum % 10
         temp=temp*10 +rem
         nnum=nnum//10
      else:
          break
print( temp)
if (temp ==num):
    print("The number is paliandrome")
else:
     print("The number is not paliandrome")