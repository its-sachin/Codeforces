import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353

def check(s,m):
    c=0; i=0
    while(i<n and c<m):
        if(s[i]==0):c+=1
        i+=1
    o = sum(s) - (i-c+1)
    while (i<n):
        if(o<=m):return True
        if(s[i]==1):o+=1

for _ in range(int(input())):
    s=input().rstrip(); n = len(s);s = [int(i) for i in s]
    l = 0
    r = min(sum(s),n-sum(s))
    while(l<=r):
        m = (l+r)//2
        if(check(s,m)):
            l+=1
        else:r-=1
    print(r)
    
    

    

    


