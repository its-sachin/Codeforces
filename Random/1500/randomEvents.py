for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    prob = []
    isS = True
    for i in range(n-1,0,-1):
        if(a[i]!=i+1):
            isS = False
            notI=i+1
            break
    ans=1
    for i in range(m):
        r,p = input().split()
        r,p=int(r),float(p)

        if(not isS and r>=notI):
            ans*=(1-p)
    if(isS):
        print(1)
    else:
        print(1-ans)


