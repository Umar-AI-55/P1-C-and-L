#Write a program that contiues to ask for a number nutil the correct number is guessed.
password = 123
num = int(input("Enter your three-digit password: "))
while num != password:
    print("Incorrect 🙁 !! Please enter your correct password.")
    num = int(input("Enter your three-digit password: "))
print("Your password is correct.")