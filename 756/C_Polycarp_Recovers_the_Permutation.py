for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mx = max(a)
    if(a[0] != mx and a[-1] != mx): print(-1); continue

    a1 = []; a2 = []
    start = 0; end = n-1;
    while(start <= end):
        if(a[start] >= a[end]):
            a1.append(a[start]); start += 1
        else:
            a2.append(a[end]); end -= 1
    a1 = a1[::-1]
    a1.extend(a2)
    print(*a1)