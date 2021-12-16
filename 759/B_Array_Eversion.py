for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    mn = max(a)
    count = 0
    curr = n-1
    prev = -1
    while a[curr] != mn:
        if(prev == -1 or a[curr] > a[prev]):
            count += 1
            prev = curr
        curr -= 1

    print(count)
