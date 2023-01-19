#square of n numbers

num=int(input("Enter the number upto whose squares are to be determined: "))
print("Square of first",num,"numbers are: ")
square=[i*i for i in range(num+1)]
print(square)