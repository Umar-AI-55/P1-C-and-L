#Create a programe that checks if a given string is palindrome.
str=str(input("Please Type here: "))
if str==str[:: -1]:
    print(str,"is a palindrome.")
else:
    print(str,"is not a palindrome.")

