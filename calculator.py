#program to generate simple calculator

print("select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
operator = int(input("Enter 1/2/3/4 : "))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operator == 1:
    print("Addition:",num1 + num2)

if operator == 2:
    print("Subtraction:",num2 - num1)

if operator == 3:
     print("Product:",num1 * num2)

if operator == 4:
    print("Quotient : ",num2/num1)
else:
    print("invalid option")

