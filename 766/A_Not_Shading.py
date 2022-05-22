for _ in range(int(input())):
    n,m,r,c = map(int,input().split())
    a = []; got = False
    for i in range(n):
        a.append(input())
        if(not got and 'B' in a[-1]):got=True
    if(not got):print(-1)
    elif(a[r-1][c-1]=='B'):print(0)
    else:
        got=False
        for i in range(m):
            got = got or (a[r-1][i]=='B')
        for i in range(n):
            got = got or (a[i][c-1] == 'B')
        print(1) if got else print(2)