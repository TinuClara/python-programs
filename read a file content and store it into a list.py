# program to read file content  and store it into a list
# using readlines()

open_file = open('data.txt','r')
file_lines = open_file.readlines()

# without using strip, newline character occurs in the output
print("File content: ")
print(file_lines)

open_file.close()

#  using strip(new line character is removed)
print("File content after removing newline character: ")
file_lines = [i.strip() for i in file_lines]
print(file_lines)
open_file.close