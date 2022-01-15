for _ in range(int(input())):
    a = list(map(int,input().split()))
    print(a[0],a[1],a[-1]-a[0]-a[1])