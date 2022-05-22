for _ in range(int(input())):
    n,m = map(int,input().split())
    a =[];ans = 26*m
    for i in range(n):
        s = input()
        for j in a:
            c=0
            for k in range(m):
                c+=abs(ord(j[k])-ord(s[k]))
            ans=min(ans,c)
        a.append(s)
    print(ans)
