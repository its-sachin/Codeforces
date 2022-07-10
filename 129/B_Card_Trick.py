import math,sys;input=sys.stdin.readline;from collections import Counter; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m = int(input())
    b=list(map(int,input().split()));prev=0
    for i in range(m):
        if(prev+b[i]<n):prev=prev+b[i]
        else:prev=b[i]+prev-n
    print(a[prev])

