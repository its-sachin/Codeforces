for _ in range(int(input())):
    n=int(input())
    d=[]
    for i in range(n):
        a=list(map(int,input().split()))
        k=0
        for j in range(a[0]):
            k=max(a[j+1]-j,k)
        d.append((k,a[0]))

    d.sort()
    p=0
    s=0
    for i in range(n):
        p=max(p,d[i][0]-s)
        s+=d[i][1]
    print(p+1)
