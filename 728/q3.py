import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
for _ in range(II()):
    n = II()
    d = L()
    d.sort()
    if(n>2):
        k=1
        s=0
        for i in range(2,n):
            s+=k*d[i]-d[i-2]*(n-i)
            k+=1
        print(-1*s)
    else:
        print(0)