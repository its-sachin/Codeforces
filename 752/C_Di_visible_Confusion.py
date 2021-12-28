import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
mx = 10**9
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(a[0]%2 == 0):print('NO');continue

    k = 2; isit = True
    for i in range(1,n):
        k = lcm(k,i+2)
        if(k>mx):break
        if(a[i]%k == 0):
            isit=False; break

    print('YES' if isit else 'NO')
