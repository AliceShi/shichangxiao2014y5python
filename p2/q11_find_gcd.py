# q11_find_gcd.py

def gcd(n1, n2):
    if n1 > n2:
        small=n2
        big=n1
    else:
        small=n1
        big=n2

    if small == 0:
        return big
    else:
        return gcd(small, big-small)


n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))


print(gcd(n1,n2))
   



        
