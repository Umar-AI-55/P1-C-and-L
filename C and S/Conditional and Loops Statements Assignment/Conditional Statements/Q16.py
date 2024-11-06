#Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
num1=float(input("Enter first side of triangle: "))
num2=float(input("Enter second side of triangle: "))
num3=float(input("Enter third side of triangle: "))
if num1==num2==num3:
    print("Hence all the three sides fo triangle are equal to each other, so it proves that the the triangle is an Equilateral Triangle.")                                
elif num1==num2!=num3 or num1!=num2==num3 or num1==num3!=num2:
    print("Hence the two sides fo triangle are equal to each other, so it proves that the the triangle is an Isosceles Triangle.")
else:
    print("Hence the sides fo triangle are different, so it proves that the the triangle is a Scalene Triangle.")
    