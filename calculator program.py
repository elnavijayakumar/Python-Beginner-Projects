# python calculator

num1 = float(input("enter number1: "))
num2 = float(input("enter number2: "))
operator = input("enter an operator (+ - * /): ")

if operator == "+":
    print(num1+num2)
elif operator =="-":
    print(round(num1-num2,2))
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(round(num1/num2,3))
else:
    print("NOT a valid operator")
