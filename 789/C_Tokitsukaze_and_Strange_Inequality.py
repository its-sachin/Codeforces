import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):   
    n = int(input())
    a = list(map(int,input().split()))
    aage = [None]*n
    for i in range(n):
        aage[i] = [0]*n
        for j in range(i+1,n):
            if(a[j]<a[i]):aage[i][j]=1
            aage[i][j]+=aage[i][j-1]
        for j in range(n):
            aage[i][j] = aage[i][-1]-aage[i][j] 
            if(i>0):aage[i][j]+=aage[i-1][j]
    # for i in aage:(print(i))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            diff = 0
            if(a[j]>a[i]):
                ans += aage[j-1][j]-aage[i][j]
                diff += aage[j][j]-aage[j][j-1]
                
                    
    # for i in aage:print(i,aage[i])
    print(ans)