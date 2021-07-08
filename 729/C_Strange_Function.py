import math
mod = 10**9+7
for _ in range(int(input())):

    n = int(input())
    f = 1
    i = 2
    s = n
    while(f<=n):
        s+=n//f
        f = (f*i)//math.gcd(i,f)
        i+=1
    print(s%mod)