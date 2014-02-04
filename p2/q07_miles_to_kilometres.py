# q07_miles_to_kilometres.py
print("Miles Kilometers Kilometres Miles")


for miles in range(1,11):
    kilometers = 1.609*miles
    kilometers1 = 15 + 5*miles
    miles1 = kilometers1/1.609

    miles = str(miles)
    kilometers = str("{0:.3f}".format(kilometers))
    kilometers1 = str(kilometers1)
    miles1 = str("{0:.3f}".format(miles1))
    
    s1 = (6-len(miles))*" "
    s2 = (11-len(kilometers))*" "
    s3 = (11-len(kilometers1))*" "

    print("{0}{1}{2}{3}{4}{5}{6}".format(miles,s1,kilometers,s2,kilometers1,s3,miles1))
