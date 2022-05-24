# from arithmaticOp import addition
# from arithmaticOp import subtract
# from arithmaticOp import multiply
# from arithmaticOp import divide
import arithmaticOp
# def add(a, b):
#     return  a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     return a / b


while True:
    print('*'*50)
    print('Calculator App')
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number: "))
    op = input("Enter the operation: (+, -, *, /): ")

    if op == '+':
        result = arithmaticOp.addition(a, b)
    elif op == '-':
        result = arithmaticOp.subtract(a, b)
    elif op == '*':
        result = arithmaticOp.multiply(a, b)
    elif op == '/':
        result = arithmaticOp.divide(a, b)
    else:
        print('Enter a valid operator')
    print(a, op, b, ' = ', result)

    d = input("Do you wish to quit? Please type ( Y, y, N, n ): ")
    if d == "Y" or d == "y":
        print("Thank you")
        break
    elif d == "N" or d == "n" :
        print("Start again :)")
    elif d != "Y" or d != "y" : 
        print("Please enter a valid choise")