for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        while(a[i]>n):a[i]>>=1
    c = {};
    d={i:False for i in range(1,n+1)}
    for i in a:
        if(c.get(i)!=None):c[i]+=1
        else:c[i]=0
        d[i]=None
    h = list(set(a));h.sort()
    got=True
    for i in h:
        k = c[i]
        l = i
        while(l>0 and k>0):
            l>>=1
            if(d.get(l)!=None):
                d[l]=None
                k-=1
        if(k>0):got=False;break
    
    for i in d:
        if(d[i]==False):got=False;break

    print('YES' if got else 'NO')



    
    
