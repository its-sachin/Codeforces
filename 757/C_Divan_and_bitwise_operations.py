MOD = int(1e9+7)
for _ in range(int(input())):
    n,m = map(int,input().split())
    s = 0
    for i in range(m):
        l,r,k = map(int,input().split())
        s |= k
    print(s*pow(2,n-1,MOD)%MOD)