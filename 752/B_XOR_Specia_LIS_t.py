for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(n&1):
        isit = True
        for i in range(1,n):
            if(a[i]<=a[i-1]):isit=False;break
        if(isit):print('NO');continue
    print('YES')