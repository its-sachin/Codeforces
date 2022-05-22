for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):a[i]=[a[i],b[i]]
    a.sort()
    for i in range(n):
        if(a[i][0]>k):break
        k+=a[i][1]
    print(k)