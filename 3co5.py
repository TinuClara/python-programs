import csv
#Open the csv file

with open('txt1.csv','r') as file:
    #Create a csv reader
    reader=csv.reader(file)

    # Iterate over the rows of the CSV file

    for row in reader:
        #Print therow as a listof strings
        print(row)