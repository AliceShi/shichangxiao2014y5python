# q04_determine_leap_year.py

x = int(input("Enter year: ")

if x % 4 == 0 and x % 100 == 0:
    print("Leap")
elif  x % 4 == 0 and x % 100 != 0:
    print("Non-Leap")
elif x % 4 != 0:
    print("Non-Leap")
