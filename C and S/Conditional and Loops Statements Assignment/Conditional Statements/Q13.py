# Take two numbers and an operator (+,-,*,/) and perform the corresponding operation.

num1=float(input("Enter first number : "))
operation=input("Choose an operator from the following +,-,/,*,:  ")
num2=float(input("Enter second number : "))
def calculate (num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
            if num2 == 0:
                    print("    Error.The denominator shouldn't be zero.")
            else:
                    return num1 / num2
    else:
         print("    Invalid Input or Operator.")
result = calculate (num1, num2, operation)
print("    Result:" , result)