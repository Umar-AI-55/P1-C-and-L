##Check if a given number is multiple of 3 and 5.
num= int(input("Enter any number: "))
if num%3==0 and num%5==0:
    print(num,"is the multiple of both 3 and 5")
elif num%3==0:
    print(num, "is the multiple of 3")
elif num%5==0:
    print(num, "is the multiple of 5")
else:
    print(num,"isn't the multiple of 3 or 5.")