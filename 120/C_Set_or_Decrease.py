import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ss=sum(a)
    if(ss<=k):print(0);continue
    if(n==1):print(a[0]-k);continue
    a.sort()
    cc = a.count(a[0])
    ans = min(ss-cc + max(0,a[0]*cc - k),ss-k)
    s=0;x=0
    for i in range(n-1,0,-1):
        s+=a[i]
        x+=1
        ans = min(ans,max(math.ceil((ss-s+x*a[0]-k)/(x+1)),0)+x)
    print(ans)