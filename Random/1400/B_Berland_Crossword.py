di={
    '2112':True,
    '2101':True,
    '2210':True,
    '2222':True,
    '1221':True,
    '1210':True,
    '1111':True,
    '1100':True,
    '1122':True,
    '1001':True,
    '1012':True,
    '0121':True,
    '0110':True,
    '0000':True,
    '0011':True,
}

for _ in range(int(input())):
    n,u,r,d,l = map(int,input().split())
    u=max(u-n-2,0)
    r-=n-2
    l-=n-2
    d-=n-2
    a=str(u)+str(r)+str(d)+str(l)
    print(a)
    if(di.get(a)==None):
        print("NO")
    else:
        print("YES")
