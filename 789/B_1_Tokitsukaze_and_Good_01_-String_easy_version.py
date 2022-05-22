import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):   
    n=int(input())
    s=input().rstrip()
    s=[int(i) for i in s]
    i=0;ans=0
    while(i<n):
        j=i
        while(j<n and s[j]==s[i]):j+=1
        if((j-i)&1):
            j-=1
            s[j]=1-s[j]
            ans+=1
        i=j
    print(ans)
            