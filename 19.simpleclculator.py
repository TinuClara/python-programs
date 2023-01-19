#program to find a single calculator using else if ladder

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))

print("1.ADDITION \n2.SUBTRACTION \n3.MULTIPLICATION \n4.DIVISION \n5.EXIT")
choice=int(input("Enter the choice :"))

if (choice== 1):                 #addition
    print("Sum= ",num1 + num2)

elif (choice== 2):               #subtraction
    print("Difference= ",num2-num1)

elif (choice == 3):               #multiplication
    print("Product= ",num2 * num1)

elif (choice == 4):               #division
    print("Quotient= ",num2/num1)

elif (choice == 5):               #division
    exit(0)
else:
    print("choose valid choice")