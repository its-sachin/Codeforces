for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())

    als=set()
    for i in range(n-1):
        if(a[i]+a[i+1]>=2*x):
            als.add(i)
            als.add(i+1)
        
