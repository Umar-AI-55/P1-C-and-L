#Print the reverse of a given number.
num=int(input("Enter any number (should have at least 2 digits): "))
reversed_num = int(str(num)[ : : -1])
print("Reversed number:", reversed_num)