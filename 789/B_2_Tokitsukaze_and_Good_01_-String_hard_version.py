import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):   
    n=int(input())
    s=input().rstrip()
    s=[int(i) for i in s]
    i=0;ans=0; k =0
    while(i<n):
        j=i
        while(j<n and s[j]==s[i]):j+=1
        print(i,j)
        if((j-i)&1):
            if(j-i==1):
                k-=1
                s[i]=1-s[i]
                while(j<n and s[j]==s[i]):j+=1
            else:
                s[j]=1-s[j]
                while(j<n and s[j]==s[i]):j+=1
                j+=1
            ans+=1
        i=j
        k+=1
    print(' ',ans,k)