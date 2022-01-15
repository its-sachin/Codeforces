def add(a,u,v,w):
    if (a.get(u) == None):
        a[u] = {}
    if (a.get(v) == None):
        a[v] = {}
    a[u][v] = w
    a[v][u] = w

for _ in range(int(input())):
 
    n = int(input())
    a = {}
    
    for i in range(n-1):
 
        u,v,w = map(int,input().split())
        add(a,u,v,w)

        m = -1
    
    
    print(ans(a,0,0,0))