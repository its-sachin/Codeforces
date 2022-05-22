for _ in range(int(input())):
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(input()))
    if(a[0][0]=='R'):print('YES');continue
    h=False
    for i in range(n):
        if(h):break
        for j in range(m):
            if(a[i][j]=='R'):
                got = False
                for u in range(i):
                    if(got):break
                    for v in range(m):
                        if(a[u][v]=='R'):got=True;break
                if(not got):
                    for u in range(n):
                        if(got):break
                        for v in range(j):
                            if(a[u][v]=='R'):got=True;break
                if(not got):print('YES');h=True;break
    if(not h):print('NO')
            