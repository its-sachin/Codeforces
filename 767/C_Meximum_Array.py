for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = {}; b=[]
    for i in a:
        if(d.get(i)==None):d[i]=1
        else:d[i]+=1
    suf = [0]*n
    for i in range(n+1):
        if(d.get(i)==None):suf[0]=i;break
    for i in range(1,n):
        d[a[i-1]]-=1
        suf[i]=suf[i-1]
        if(d[a[i-1]]==0):
            suf[i]=min(suf[i],a[i-1])
    k=0
    while(k<n):
        if(suf[k]==0):
            k+=1;b.append(0);continue
        seen = set(); j = k
        while(j<n and len(seen)<suf[k]):
            if(a[j]<suf[k]):
                seen.add(a[j])
            j+=1
        b.append(suf[k]); k=j

    print(len(b))
    print(*b)