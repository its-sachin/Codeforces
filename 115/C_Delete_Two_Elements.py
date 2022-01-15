for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=sum(a)
    if((2*k)%n!=0):print(0);continue
    k=2*k//n

    c = {}
    for i in a:
        if(c.get(i)):c[i]+=1
        else:c[i]=1
    ans = 0
    for i in a:
        ans += c.get(k-i,0)
        if(i==k-i): ans -= min(1,c.get(k-i,0))
    print(ans//2)
