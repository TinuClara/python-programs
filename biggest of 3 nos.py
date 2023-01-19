##find biggest no. using if

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))

if (num2< num1> num3):
    print(num1,"is greater")
elif(num1<num2>num3):
      print(num2,"is greater")
else:
   print(num3, "is greater")