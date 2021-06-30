import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
# for _ in range(II()):


def bin(n,x,i):
    l = 0
    r = n
    less=0
    more=0
    ans=1
    while(l<r):
        m=(l+r)//2
        if(i>=m):
            if(m!=i):
                less+=1
                ans*=(x-less)
            l=m+1
        else:
            more+=1
            ans*=(n-x-more+1)
            r=m
    rem=n-less-more-1
    while(rem>0):
        ans*=(rem)
        rem-=1
    return ans%(10**9+7)

n,x,i = M()
print(bin(n,x,i))
