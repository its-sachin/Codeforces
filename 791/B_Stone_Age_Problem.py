import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
n,q = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a); d = {i:a[i] for i in range(n)};v=-1
for i in range(q):
    Q=list(map(int,input().split()))
    if(Q[0]==2):s=n*Q[1];d={};v=Q[1]
    else:
        Q[1]-=1
        if(d.get(Q[1])==None):s+=Q[2]-v
        else:s+=Q[2]-d[Q[1]]
        d[Q[1]]=Q[2]
    print(s)