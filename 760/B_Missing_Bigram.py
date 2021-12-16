for _ in range(int(input())):
    n = int(input())
    a = list(input().split())
    s = a[0]
    for i in range(1,n-2):
        if(a[i][0] == s[-1]):
            s += a[i][1]
        else:
            s += a[i]
    if(len(s) < n):
        s += 'a'
    print(s)

    