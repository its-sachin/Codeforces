import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    for i in range(1,n):a[i]+=a[i-1]
    for i in range(q):
        k=int(input())
        if(a[-1]<k):print(-1);continue
        l=0;r=n-1
        while l<=r:
            m=(l+r)//2
            if(a[m]>=k):r=m-1
            else:l=m+1
        print(l+1)