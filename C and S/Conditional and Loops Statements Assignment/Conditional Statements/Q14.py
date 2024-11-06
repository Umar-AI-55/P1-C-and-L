#Check if a year input by the user is a century year.
num=int(input("Enter Year: "))
if num%100==0:
    print(num,"is the Century Year.")
else:
    print(num,"is not the Century Year.")

