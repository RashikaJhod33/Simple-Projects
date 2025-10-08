# CREAT A CALCULATER USING PYTHON

# input the two integars numbers
A = int(input("Enter the first number:"))
B = int(input("Enter the second number:"))

print("What kind of operation you perform?\n1.Press + for addition\n2.Press - for subtraction\n3.Press * for multiplication\n4.Press / for division")

# Input the operator
operator = input("Enter the operator:")

try:
    match operator:
        case "+":
            print(f"result is {A + B}.")
        case "-":
            print(f"result is {A - B}.")
        case "*":
            print(f"result is {A * B}.")
        case "/":
            print(f"result is {A / B}.")
        case "default":
            print("There was an error.")
except:
    print("Enter the valid value of A and B.")