#Take three sides of a triangle and check if they form a valid triangle.
num1=int(input("Enter First side of triangle: "))
num2=int(input("Enter Second side of triangle: "))
num3=int(input("Enter Third side of triangle: "))
# A valid triangle is the one, which two sides sum is greater than the third side.
if num1 + num2 > num3:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")