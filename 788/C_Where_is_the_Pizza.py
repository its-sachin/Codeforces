m = 10**9+7
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    dd={}
    for i in range(n):
        dd[a[i]]=i
    ans = 1
    for i in range(n):
        if(c[i] != 0 or a[i]==b[i]):continue
        j=dd[b[i]]; f=2
        while(j!=i):
            if(c[j]!=0):f=1
            c[j]=1
            j=dd[b[j]]
        ans=(ans*f)%m
        k=1
    print(ans)

