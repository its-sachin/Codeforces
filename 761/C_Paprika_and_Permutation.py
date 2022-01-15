for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    done = {}
    
    for i in range(n):
        if(a[i]<=n and a[i]>=1):
            if(done.get(a[i])):
                done[a[i]] += 1
            else:
                done[a[i]] = 1

    notdone = []; req = []
    for i in a:
        if(done.get(i) == None):
            notdone.append(i)
    for i in range(1,n+1):
        if(done.get(i)==None):
            req.append(i)

    for i in done:
        if(done[i]>1):
            notdone.extend([i]*(done[i]-1))

    notdone.sort()
    req.sort()

    valid = True
    for i in range(len(req)):
        if(notdone[i]-req[i] <= req[i]):
            valid = False
            break
    if(valid):
        print(len(req))
    else:
        print(-1)