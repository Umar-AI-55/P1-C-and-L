#Use a loop to print numbers in reverse order within a given range.
num_start = int(input("Enter the starting number: "))
num_end = int(input("Enter the ending number: "))
for num in range(num_end,num_start-1,-1):
    print(num)
print("The reversed order from the ending number to the starting number.")

