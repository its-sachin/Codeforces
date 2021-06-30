for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    d = {}
    sumN=0
    for i in a:
        if(d.get(i) is None):
            d[i]=1
        else:
            d[i]+=1
        sumN+=1
    d = list(sorted(d.values(),reverse=True))
    # print(d)
    mi = 10**7
    s=0
    for i in range(len(d),0,-1):
        prev = d[i-1]
        curr=s+sumN-(i*prev)
        if(mi>curr):
            mi=curr
        s+=prev
        sumN-=prev
    print(mi)


    