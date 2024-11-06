#Take the user's score and determine that if they pass or fail (if 50 or above).
print("Enter your score that you have got out of 100.")
num=float(input("Enter your score: "))
if num>100:
    print("Your total score is 100. Please enter your score that you have got out of 100.")
elif 100>=num>=50:
    print("Congrats! You have passed.")
else:
    print("You are failed.")