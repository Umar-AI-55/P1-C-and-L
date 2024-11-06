#Write a program to check if a number is within a specified range.
minrange=float(input("Enter minimum range: "))
maxrange=float(input("Enter maximum range: "))
num=float(input("Enter any number: "))
if maxrange<minrange:
    print("The maximum range should be greater than minimum range.")
elif num>=minrange and num<=maxrange:
    print(num,"is within the specified range.")
else:
    print(num,"is not within the specified range.")



