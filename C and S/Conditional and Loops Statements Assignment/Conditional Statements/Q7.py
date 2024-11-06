#write a program to find the largest of three numbers.
num1=int(input("Enter the First number: ")),
num2=int(input("Enter the Second number: ")),
num3=int(input("Enter the Third number: ")),
if num1>num2 and num1>num3:
    print(num1,"is the largest number.")
elif num2>num1 and num2>num3:
    print(num2,"is the largest number.")
elif num1==num2==num3:
    print("All the numbers are equal.")
else:
    print(num3,"is the largest number.")
