for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans = 0
    d={}
    for i in range(n):
        if(d.get(a[i])==None):d[a[i]]=[i]
        else:d[a[i]].append(i)
    ans=-1
    for i in d:
        if(len(d[i])>1):
            for j in range(1,len(d[i])):
                ans = max(ans,n-(d[i][j]-d[i][j-1]))
    print(ans)