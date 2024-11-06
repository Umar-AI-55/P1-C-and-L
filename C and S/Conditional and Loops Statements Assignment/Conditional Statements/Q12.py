#Write a program that takes a temporature in Celcius and checks ifit is freezing, moderate or hot.
num= int(input("Enter temperature in Celcius: "))
if num<=0:
    print (num,"°C is the Freezing Temperature.")
elif num>0 and num<=25:
    print (num,"°C is the Moderate Temperature.")
else:
    print(num,"°C is Hot Temperature.")