import math,sys;input=sys.stdin.readline;from collections import Counter; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
n,x=map(int,input().split())
if(x==1 and n>1):print(-1);exit()
d = {}
def doit(x):
    s=str(x)
    if(len(s)>=n):return 0
    else:
        if(d.get(s)!=None):return d[s]
        ans=inf
        for j in set(s):
            k=int(j)
            if(k>1):
                v=x*k
                ans=min(ans,doit(v)+1)
        d[s]=ans
        return ans
ans = doit(x)
print(-1 if ans>=inf else ans)
