def toint(x,p):
    i = int(x**(1./p))
    if((i+1)**p == x): return i+1
    return i

for _ in range(int(input())):
    n = int(input())
    print(toint(n,2) + toint(n,3) - toint(n,6))
