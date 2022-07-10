import math,sys;input=sys.stdin.readline;from collections import Counter; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    pos=True; ind=[]
    for i in range(n-1):
        m1=min(a[i+1:]);m2=min(b[i+1:])
        if(a[i]<=m1 and b[i]<=m2):continue
        elif((a[i]<m1 and b[i]>m2) or (a[i]>m1 and b[i]<m2)):pos=False;break
        got=False
        for j in range(i+1,n):
            if(a[j]==m1 and b[j]==m2):
                a[j],a[i]=a[i],a[j]
                b[j],b[i]=b[i],b[j]
                got=True
                ind.append([j+1,i+1])
                break
        if(not got):pos=False;break
    if(not pos):print(-1)
    else:
        print(len(ind))
        for i in ind:print(*i)
        
        