import csv
reader=csv=csv.reader(open("employees.csv"))
no_lines=len(list(reader))
print(no_lines)