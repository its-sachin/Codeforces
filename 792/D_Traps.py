for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = [[a[i]-(n-i-1),i] for i in range(n)]
    b.sort(reverse=True)
    for i in range(k):
        a[b[i][1]]=-1
    ans=0;st=0
    for i in range(n):
        if(a[i]==-1):st+=1
        else:ans+=a[i]+st
    print(ans)