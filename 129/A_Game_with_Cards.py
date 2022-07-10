import math,sys;input=sys.stdin.readline;from collections import Counter; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    m1,m2=max(a),max(b)
    if(m1==m2):ans=['Alice','Bob']
    elif(m1>m2):ans=['Alice']*2
    else:ans=['Bob']*2
    for i in ans:print(i)