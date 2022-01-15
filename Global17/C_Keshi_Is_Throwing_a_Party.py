import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a,b=[],[]
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai); b.append(bi)
    
    l,r = 1,n+1
    while(r-l>1):
        m = (l+r)>>1
        c = 0
        for i in range(n):
            if(a[i]>=m-1-c and b[i]>=c):
                c+=1
        if(c>=m):
            l=m
        else:
            r=m
    print(l)