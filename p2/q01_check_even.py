# q01_check_even.py

number = int(input("Enter the number: "))

if number % 2 == 0:
    x = "even"
else:
    x = "odd"

print("{0} is {1}".format(number,x))
