for _ in range(int(input())):
    n,m = map(int,input().split())
    a=[]
    for i in range(n):
        for j in range(m):
            a.append(max(i,n-i-1)+max(j,m-j-1))
    print(*sorted(a))