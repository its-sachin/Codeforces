for _ in range(int(input())):
    a=list(map(int,input().split()))
    a.sort()
    if(a[-1]!=a[0]+a[1]):
        if((a[0]==a[1] and a[-1]%2==0) or (a[1]==a[2] and a[0]%2==0) ):print('YES')
        else:print('NO')
    else:print('YES')