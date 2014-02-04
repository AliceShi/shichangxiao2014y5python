# q02_triangle.py

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a + b > c and a + c > b:
    p = a + b + c
    print("perimeter = {0}".format(p))
else:
    print("Invalid triangle!")
    
