# q04_determine_leap_year.py

x = int(input("Enter year: "))

if x % 400 == 0:
    print("Leap")
elif x % 100 == 0:
    print("Non-leap")
elif x % 4 == 0:
    print("Leap")
else:
    print("Non-leap")
