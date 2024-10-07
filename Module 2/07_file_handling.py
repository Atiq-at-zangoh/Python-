### FILE HANDLING

file = open("Module 2/02_tuples", 'r')

text = file.readline()

print(text)

file.close()

## Second way

with open("Module 2/02_tuples", 'r') as file:
    print(file.readline())

#   No need to close

###  Create new file

with open("Module 2/file.txt", 'w') as file:
    file.writelines(["This is the new file...", "\nThis is second line", "\nthis is third line"])

with open("Module 2/file.txt", 'a') as file:
    file.writelines(["append new line...", "\nThis is second appended line", "\nthis is third appended line"])

## Read a file

with open("Module 2/file.txt", 'r') as file:
    print(file.read())

with open("Module 2/file.txt", 'r') as file:
    print(file.read(10))


with open("Module 2/file.txt", 'r') as file:
    print(file.readline())

with open("Module 2/file.txt", 'r') as file:
    print(file.readlines())
