def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error: Division by zero."
    else:
        return "Error: Invalid operator."

while(1):
  print("1.For Addition")
  print("2.For Subtraction")
  print("3.For Multiplication")
  print("4.For Division")
  print("0.For Exit")
  ch=int(input("Enter Your Choice:"))
  if ch==1:
      x=int(input("Enter first number:"))
      y=int(input("Enter second number:"))
      op=input("Enter an operator:")
      print("Sum of two number is:")
      print(calculate(x,y,op))
  elif ch==2:
      x=int(input("Enter first number:"))
      y=int(input("Enter second number:"))
      op=input("Enter an operator:")
      print("Subtraction of two number is:")
      print(calculate(x,y,op))
  elif ch==3:
      x=int(input("Enter first number:"))
      y=int(input("Enter second number:"))
      op=input("Enter an operator:")
      print("Multiplication of two number is:")
      print(calculate(x,y,op))
  elif ch==4:
      x=int(input("Enter first number:"))
      y=int(input("Enter second number:"))
      op=input("Enter an operator:")
      print("Division of two number is:")
      print(calculate(x,y,op))
  elif ch==0:
       print("Exit From The Program")
       break
  else:
       print("Invalid Operator. Please Enter The Correct Operator")
