for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    p = False
    for i in range(n):
        if(b[i]-a[i] not in (0,1)):print('NO');p = True;break
    if(not p):print('YES')

    