
# if else

bill = float(input("Enter Bill Aomunt"))
discount = 10

# if bill>100.0:
#     print("You will get {} % discount".format(discount))

# else:
#     print("You will not get discount")    


# if ladder

if bill>=200:
    print("You will get 20 % discount")

elif bill<200 and bill>100:
    print("You will get 10 % discount")

else:
    print("You are not eligible for discount")


# nested if

age = int(input("Enter your age : "))

if age>=0:
    if age>18:
        print("You are eligible to cast a vote")

    else:
        print("You are not eligible for vote")

else:
    print("Age can't be negative or zero")                         

