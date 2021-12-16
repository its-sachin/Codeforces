for _ in range(int(input())):
    n =  int(input())
    a = list(map(int,input().split()))
    a = [[a[i],i] for i in range(n)]
    a.sort()
    b = [0]*n; j = 1; s = 0
    for i in range(n-1,-1,-2):
        b[a[i][1]] = j; s+= a[i][0]*j
        if(i-1>=0):
            b[a[i-1][1]] = -1*j; s+= a[i-1][0]*j
        j+=1
    b.insert(0,0)
    print(2*s)
    print(*b)