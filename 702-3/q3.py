import math

def isCube(a):
    return round(a ** (1 / 3)) ** 3 == a


def strout(n):
    k = 1
    while(k**3 < n):
        if (isCube(n-k**3)):
            return ("YES")   
            break
        else:
            k += 1
    return "NO"


testCases = int(input())
while (testCases > 0) :
    n = int(input())
    print(strout(n))
    
    testCases -= 1;
