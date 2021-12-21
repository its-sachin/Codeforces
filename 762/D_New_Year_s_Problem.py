for _ in range(int(input())):
    input()
    m,n = map(int,input().split())
    p = []
    # (val,shop,friend)
    for i in range(m):
        a = list(map(int,input().split()))
        for j in range(n):
            p.append([a[j],i,j])
    p.sort(); got = False
    sf = set(); ss = set()
    for i in range(m*n-1,-1,-1):
        sf.add(p[i][2])
        if(p[i][1] in ss):
            got = True
        ss.add(p[i][1])
        if(len(sf)==n and got):
            ans = p[i][0]
            break
    print(ans)
