for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        if(d.get(i)==None):d[i]=1
        else:d[-1*i]=1
    c=0
    for i in d:c+=d[i]
    print(c)