
# For loop

for i in range(10):
    print(i)

cars = ["Swift", "Creta", "Fortuner", "Rolls Royce"]

for car in cars:
    print(car)

for index, car in enumerate(cars):
    print(index,car)

# While loop

count=0

while count<len(cars):
    print(cars[count])
    count+=1

# Nested for loop

for i in range(10):
    for j in range(10):
        print(0, end=" ")
    print()