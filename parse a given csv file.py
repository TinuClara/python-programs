import csv
csv_string="""1,2,3
              4,5,6
              7,8,9"""
print("original string:")
print(csv_string)
lines=csv_string.splitlines()
print("List of csv formatted strings: ")
print(lines)
reader=csv.reader(lines)
parsed_csv=list(reader)
print("/n List representation of csv file: ")
print(parsed_csv)