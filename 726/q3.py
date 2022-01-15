for _ in range(int(input())):

    n = int(input())
    a = [int(x) for x in input().split()]

    a.sort()

    diff = a[1]-a[0]
    l=0

    for i in range(1,n-1):
        c = a[i+1] -a[i]
        if (c<diff):
            diff=c
            l=i

    o = a[l]
    z = a[l+1]

    print(o, *a[l+2:], *a[:l], z)

    