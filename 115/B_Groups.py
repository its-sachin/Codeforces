for _ in range(int(input())):
    n=int(input())
    d = {i:{} for i in range(5)}
    for i in range(n):
        a=list(input().split())
        for j in range(5):
            if(a[j]=='1'):d[j][i]=True

    pos = []
    for i in d:
        if(len(d[i])>=n//2):pos.append(d[i])
    got = False
    for i in range(len(pos)):
        for j in range(i+1,len(pos)):
            isit = True
            for k in range(n):
                if(pos[i].get(k) == None and pos[j].get(k) == None):
                    isit = False
                    break
            if(isit):
                got=True
                break
    print('YES' if got else 'NO')