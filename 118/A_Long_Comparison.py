for _ in range(int(input())):
    x1,p1 = map(int,input().split())
    x2,p2 = map(int,input().split())

    p1 += len(str(x1))
    p2 += len(str(x2))

    if(p1==p2):
        p1,p2=x1/(10**len(str(x1))),x2/(10**len(str(x2)))

    if(p1==p2):print('=')
    elif(p1<p2):print('<')
    else:print('>')