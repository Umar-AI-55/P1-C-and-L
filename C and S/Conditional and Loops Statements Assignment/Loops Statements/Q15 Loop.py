#Print the sum of even and odd numbers separately up to a given number.
even_sum = 0
odd_sum = 0
for num in range(1, 51):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
