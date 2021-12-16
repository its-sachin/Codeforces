for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(1,2*n,2):
        a[i-1],a[i] = a[i], a[i-1]
    if(n>1):
        if(a[-1] == (a[-2] + a[0])/2 or a[0] == (a[1]+a[-1])/2):
            a[-1],a[0] = a[0],a[-1]
    print(*a)
