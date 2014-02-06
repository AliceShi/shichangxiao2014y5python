# q12_find_factors.py

def pFactors(n): 
        
        import math 
        pFact = []
        check = 2
        for check in range(2, int(math.sqrt(n)+1)): 
             while n % check == 0: 
                pFact.append(check) 
                n /= check 
        if n > 1: 
          pFact.append(n) 
        return pFact
        
n = int(input("Enter an integer: "))
print (pFactors(n))



