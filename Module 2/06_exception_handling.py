## Exceptions

# print(34/0) Exception occured

try:
    print(34/0)

except ZeroDivisionError as zde:
    print("Can't divide by 0", zde)

except Exception as e:
    print("Something going wrong")
    print(e)
    print(e.__class__)


