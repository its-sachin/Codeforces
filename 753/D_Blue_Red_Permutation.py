for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    color = input()
    blue = []; red = []
    for i in range(n):
        if(color[i] == 'B'):blue.append(a[i])
        else:red.append(a[i])
    blue.sort(); red.sort()
    got = True
    for i in range(len(blue)):
        if(blue[i] < i+1):
            got = False
            break
    if(not got): print('NO');continue
    k = len(blue)
    for i in range(len(red)):
        if(red[i] > i+1+k):
            got = False
            break
    print('YES' if got else 'NO')