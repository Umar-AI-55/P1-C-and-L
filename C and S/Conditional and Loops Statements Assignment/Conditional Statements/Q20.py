#Write a program to evaluate that if the inputted number is prime or not.
num = int(input("Enter any number: "))
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print(num, "is a prime number.")
else:
    print(num, "isn't a prime number.")