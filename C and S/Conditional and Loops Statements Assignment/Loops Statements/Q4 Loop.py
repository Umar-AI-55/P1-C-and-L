#Print the multiplication table of a given number.
num = int(input("Enter a number to get the multiplication table of the number: "))
def multiplication_table(num):
    for i in range(1, 11):
         print(f"{num} * {i} = {num * i}")
multiplication_table(num)