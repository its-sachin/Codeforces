for _ in range(int(input())):
    n  =int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = [[a[i],i] for i in range(n)] 
    b = [[b[i],i] for i in range(n)]

    a.sort(reverse=True)
    b.sort(reverse=True)
    d = {}
    for i in range(n):
        d[a[i][1]],d[b[i][1]] = True,True
        if(len(d) == i+1):
            num = i+1
            break
    s = [0]*n
    for i in range(num):
        s[a[i][1]] = 1
    for i in s:
        print(i,end="")
    print()

