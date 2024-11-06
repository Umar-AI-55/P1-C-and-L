#Ask the user for a grade percentage and display the corresponding letter grade (A,B,C,D,F).
print("Enter your marks that you have got out of 100 and then press enter to get your grade.")
num=int(input("Enter your marks: "))
if 100>=num>=90:    
    print("Your grade is A")
elif num>100:
    print("Please enter your marks within the range of 100 and 0")    
elif 90>num>=80:
    print("Your grade is B")
elif 80>num>=70:
    print("Your grade is C") 
elif 70>num>=50:
    print("Your grade is D") 
else:
    print("Your grade is F")

