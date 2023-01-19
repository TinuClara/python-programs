# Python program to write a python dictionary to a csv file
# After writing the csv file read the csv file and display the content

import csv

# Data to be inserted

data=[{'Name':'Anu','Age':'23','Country':'India'},
      {'Name':'Sebin','Age':'22','Country':'United states'},
      {'Name':'Anugraha','Age':'21','Country':'Singapore'},
      {'Name':'Anupama','Age':'26','Country':'United States'}]

# Write to csv file
with open('people.csv','w') as csvfile:
    headnames=['Name','Age','Country']
    csvwriter=csv.DictWriter(csvfile,fieldnames=headnames)
    csvwriter.writeheader()
    for row in data:
        csvwriter.writerow(row)

# Readfrom csv file and print contents
with open('people.csv','r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)


