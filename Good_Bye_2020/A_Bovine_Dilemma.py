for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = set()
    for i in range(n):
        for j in range(i+1,n):
            s.add(a[j]-a[i])
    print(len(s))