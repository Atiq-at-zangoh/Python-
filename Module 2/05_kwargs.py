# args

def add(a,b):
    return a+b

print(add(4,5))
# print(add(4,5,6)) error

def addition(*args):

    sum=0
    for i in args:
        sum+=i 

    return sum


print(addition(1,2,3,4,5))


###### kwargs

def total(**kwargs):

    totals = 0
    for i,j in kwargs.items():
        totals+=j

    return totals

print(total(Fruits= 80, Veggies= 54, Toffee=200))


