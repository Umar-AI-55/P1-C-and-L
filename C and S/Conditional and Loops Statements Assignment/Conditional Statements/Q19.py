#Check if a string input is uppercase, lowercase or a mix.
str=str(input("Please type here: "))
if str.isupper():
    print("The string is uppercase.")
elif str.islower():
    print("The string is lowercase.")
else:
    print("The string is mix.")