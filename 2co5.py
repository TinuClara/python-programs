#Program to copy odd lines of one file to another

#Opening files for reading
a=open('data.txt')
output_file=open('writedata.txt','w')

# Coping/reading contents from read_file to copy_data
copy_data =a.readlines()
print("\nActual file content is: ")
print(copy_data, "\n")


for i in range(0, len(copy_data)):
    if i % 2 == 0:
        output_file.write(copy_data[i])
    else:
        pass

# Closing file after writing
output_file.close()

# Opening write file in read mode and printing values
output_file=open('Writedata.txt','r')
print("Odd lines in the text is: ")
print(output_file.read())


#Closing files
a.close()
output_file.close()

