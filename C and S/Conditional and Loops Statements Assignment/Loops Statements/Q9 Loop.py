#Write a program to print the first 10 Fibonacci numbers.
input("Press Enter to gat the first ten Fabonacci numbers:")
x, y = 0, 1
for _ in range(10):
    print(x, end=" ")
    x, y = y, x + y
print("First 10 Fabonacci numbers.")





