for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    avg=sum(a)/n;pos=False
    for i in a:
        if(i==avg):pos=True;break
    print ("YES" if pos else "NO")