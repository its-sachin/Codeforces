for _ in range(int(input())):
    a,b=map(int,input().split())
    d={}
    if(a<b):
        a,b=b,a

    def f(k1,k2,a,b):
        l=max(0,k1-a,a-k2)
        r=min(k1,a,a+b-k2)

        # print(k1,k2,l,r)
        for i in range(l,r+1):
            
            # print(i,a+k1-(2*i))
            if(d.get(a+k1-(2*i))==None):
                d[a+k1-(2*i)]=True

    h=(a+b)//2
    if(h==(a+b)/2):
        f(h,h,a,b)
    else:
        f(h,h+1,a,b)
        f(h+1,h,a,b)

    print(len(d))
    d=[i for i in d]
    d.sort()
    for i in d:
        print(i,end=' ')
    print('')