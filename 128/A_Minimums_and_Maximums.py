for _ in range(int(input())):
    l1,r1,l2,r2 = map(int,input().split())
    if(l1<=l2):
        if(l2<=r1):print(l2)
        else:print(l2+l1)
    else:
        if(l1<=r2):print(l1)
        else:print(l1+l2)
