for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=a[0]
    for i in a:
        ans=i&ans
    print(ans)