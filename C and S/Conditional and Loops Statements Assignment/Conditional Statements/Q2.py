#Take the users age as input and display whether they are minor, adult or senior citizen.
age=int(input("Enter Your Age: "))
if 0<age<18:
    print("You are minor.")
elif 50>age>=18:
    print("You are adult.")
else:
    print("You are a senior citizen.")
