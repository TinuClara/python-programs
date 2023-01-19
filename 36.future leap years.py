# future leap years from current year to a final year entered by user.

year=int(input("Enter the year upto which the leap is to be finded:"))
for i in range(2022,year+1):
    if(i%4==0) and (i%100!=0):
        print(i)
    if(i%100==0) and (i%400==0):
        print(i)