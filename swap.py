#swap two variables

var = int(input("Enter the value of first variable :"))
num = int(input("Enter the value of second variable :"))
temp = var
var = num
num = temp
print("First variable is: ",var,"and second variable is: ", num)