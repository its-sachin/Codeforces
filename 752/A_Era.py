import math; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    k=1;ans=0
    for i in range(n):
        if(a[i]>k):
            ans+=a[i]-k
            k=a[i]
        k+=1
    print(ans)