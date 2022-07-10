for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=[a[1],a[0]]
    i=2;j=n-1
    while i<=j:
        b.append(a[j])
        if(i!=j):
            b.append(a[i])
        i+=1;j-=1
    print(b)
    