import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353

def check(s,m):
    o=0;i=0;z=0
    while i < n and z < m:
        if(s[i] == 0):z+=1
        else:o+=1
        i+=1
    if(z<m):return False
    while i<n and s[i]==1 : i+=1;o+=1
    k=sum(s)-o;p=0
    while k > m:
        if(i >= n):return False
        while p<n and s[p]==1:p+=1;k+=1
        p+=1;i+=1
        while i<n and s[i]==1:i+=1;k-=1
    return True

for _ in range(int(input())):
    s=input().rstrip(); n = len(s);s = [int(i) for i in s]
    l = 0
    r = min(sum(s),n-sum(s))
    while(l<r):
        m = (l+r)//2
        if(check(s,m)):r=m
        else:l=m+1
    print(l)
    
    

    

    


