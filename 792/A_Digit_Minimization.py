import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):
    n=input().rstrip()
    if(len(n)==2):print(n[1])
    else:print(min(n))