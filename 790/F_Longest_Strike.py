import math,sys;input=sys.stdin.readline;from collections import Counter; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=Counter(a)
    a=[i for i in c];a.sort()
    ans=0;cnt=0;op=[];i=0;n=len(a)
    while i<n:
        if(c[a[i]]>=k):
            j=i+1
            while(j<n and a[j]==a[j-1]+1 and c[a[j]]>=k):j+=1
            if(op==[] or op[1]-op[0]<a[j-1]-a[i]):op=[a[i],a[j-1]]
            i=j
        else:i+=1
    if(op==[]):print(-1)
    else:print(op[0],op[1])
        

            
    