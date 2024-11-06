#Write a program that breaks the loop when a certain condition is met.
n = 5
for i in range(1,6):
    print("N:", i)
    if i == n:
        print("Loop ended due to break.")
        break
        print("The loop has ended.")# this line will not exicuted because of break.