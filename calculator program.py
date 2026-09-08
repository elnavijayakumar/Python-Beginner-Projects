# python calculator

num1 = float(input("enter the number1: "))
num2 = float(input("enter the number2: "))
operator = input("enter an operator (+ - * /): ")

if operator == "+":
    print(num1+num2)
elif operator =="-":
    print(round(num1-num2,2))
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(round(num1/num2))
else:
    print("NOT an valid operator")