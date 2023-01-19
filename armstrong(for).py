#to check whether a number is armstrong or not

temp=0
num=int(input("Enter the number to check whether it is armstrong or not: "))
nnum=num
for i in range(nnum):
      if nnum > 0:
        rem=nnum % 10
        temp=temp +rem * rem * rem
        nnum=nnum//10

      else:
          break
print( temp)
if (temp == num):
    print("The number is armstrong")
else:
     print("The number is not armstrong")