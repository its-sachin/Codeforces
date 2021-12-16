for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    i = n-1; j = n-k-1
    s = 0
    for l in range(k):
        s += a[j]//a[i]
        i -= 1; j-=1
        l += 1
    for i in range(n-2*k-1,-1,-1):
        s += a[i]

    print(s)