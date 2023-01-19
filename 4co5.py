import csv


#specify the column indices that you want to read
columns_to_read= [0, 2]

#open the csv file and readthe contents
with open('worksheet.csv','r') as f:
    #Create a csv reader
    reader=csv.reader(f)

    # Iterate over the rows of the CSV file
    for row in reader:
        #Print therow as a listof strings
        print([row[i] for i in columns_to_read])