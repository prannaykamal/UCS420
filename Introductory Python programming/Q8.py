#8.1
def divide(a,b):
    try:
        x=a/b
    except ZeroDivisionError:
        return "division by zero"
    return x

#8.2
def input_integer():
    try:
        x=int(input("enter integer "))
        return x
    except ValueError:
        return "enter a valid integer"

#8.3
def division(a,b):
    try:
        x=a/b
        return x
    except ZeroDivisionError:
        return "division by zero"
    finally:
        print("division by zero using try-except block is completed")

print(divide(2,0))
print(divide(3,2))
print(input_integer())
print(division(3,0))
