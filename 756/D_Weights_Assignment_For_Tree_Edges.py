for _ in range(int(input())):
    n = int(input())
    anc = list(map(int,input().split()))
    p = list(map(int,input().split()))
    for i in range(n): anc[i]-=1; p[i]-=1
    d = [-1]*n; w = [-1]*n
    for i in range(n):
        if(anc[i] == i):
            root = i
    if(p[0] != root):
        print(-1); continue
    d[root] = 0; done = False; w[root] = 0
    for i in range(1,n):
        if(anc[p[i]] == root):
            d[p[i]] = d[p[i-1]] + 1; w[p[i]] = d[p[i]]
        else:
            if(d[anc[p[i]]] == -1):
                print(-1); done = True; break
            else:
                d[p[i]] = d[p[i-1]] + 1; w[p[i]] = d[p[i]] - d[anc[p[i]]]

    if not done: print(*w)