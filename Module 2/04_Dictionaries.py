# DICTIONARIES

my_dict = {1:"Python", 
           2: "Ruby",
           3: "C++"
           }

print(my_dict)

my_dict[2] = "Java"
print(my_dict)

del my_dict[3]
print(my_dict)

my_dict[3] = "Fortran"
print(my_dict)

my_dict[4] = "COBOL"
print(my_dict)

for item in my_dict.items():
    print(item)

for key, value in my_dict.items():
    print(key,value)

my_dict.pop(1)
print(my_dict)  

my_dict.popitem()
print(my_dict)
