#Generate all factors of a number.
factors=[]
num=int(input("Enter the number: "))
for i in range(1,num+1,1):
    if num%i==0:
        factors.append(i)
print("The factors of the number",num,"are: ",factors)
