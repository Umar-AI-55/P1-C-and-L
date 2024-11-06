#Write a program that asks for an integer and checjs if it is divisible by 2 or 3 or both.
num= int(input("Enter any number: "))
if num%2==0 and num%3==0:
    print(num,"is divisible by both of 2 and 3")
elif num%2==0:
    print(num, "is divisible by 2")
elif num%3==0:
    print(num, "is divisible by 3")
else:
    print(num,"isn't the divisible of 2 or 3.")