import math,sys;input=sys.stdin.readline;from collections import Counter; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353

for _ in range(int(input().rstrip())):
    n=int(input().rstrip())
    adj={i:[] for i in range(1,n+1)}
    for i in range(n-1):
        u,v=map(int,input().rstrip().split())
        adj[u].append(v)
        adj[v].append(u)

    count = {i:0 for i in range(1,n+1)}
    vis = [False]*n
    def setc(i):
        c=0;vis[i-1]=True
        for j in adj[i]:
            if(not vis[j-1]):
                c+=setc(j)
        count[i]=c
        return c+1

    def ans(i):
        pos = []
        for j in adj[i]:
            if(count[j]<count[i]):
                pos.append(j)
        if(len(pos)==2):
            pos = []
            for j in adj[i]:
                if(count[j]<count[i]):
                    pos.append(j)
            return max(count[pos[0]]+ans(pos[1]),count[pos[1]]+ans(pos[0]))
        elif(len(pos)==1):
            return count[pos[0]]
        else:return 0
        
    setc(1)
    # print(count)
    print(ans(1))
