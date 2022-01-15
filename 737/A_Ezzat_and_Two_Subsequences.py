for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s=0
    m=a[0]
    for i in a:
        m=max(m,i)
        s+=i
    s-=m
    print((s/(n-1))+m)
