for _ in range(int(input())):
    n,l,r,k = map(int,input().split())
    a = list(map(int,input().split()))  
    a.sort()
    s = 0; c = 0
    for i in range(n):
        if(a[i]>=l and a[i]<=r):
            s += a[i]
            c += 1
        if(s>k):
            c-=1
            break

    print(c)