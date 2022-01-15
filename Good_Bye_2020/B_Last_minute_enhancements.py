for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c = 0; d ={}; i =0
    for i in range(n):
        if(d.get(a[i])==None):c+=1;d[a[i]]=True
        elif(d.get(a[i]+1)==None):c+=1;d[a[i]+1]=True
    print(c)