operator= input("Please enter an operator(+ - * /): ")

num1= float(input("Please enter the first number: "))
num2= float(input("Please enter the second number: "))

if operator == "+":
  print(num1+ num2)

elif operator == "-":
  print(num1- num2)

elif operator == "*":
  print(num1* num2)

elif operator == "/":
  print(num1/ num2)
  
else:
  print("Please enter a valid operator")
  
