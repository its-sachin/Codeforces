for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = a[0]
    for i in range(1,n):
        ans = max(ans,a[i]-a[i-1])
    print(ans)