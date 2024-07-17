def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print(divide_numbers(x,y))
