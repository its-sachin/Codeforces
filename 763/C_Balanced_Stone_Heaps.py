for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l = 0; r = max(a)
    while (l<=r):
        x = (r+l)//2
        c = a[:]; isit = True
        for i in range(n-1,1,-1):
            d = max(min(a[i],(c[i]-x))//3,0)
            c[i] -= 3*d
            c[i-1] += d
            c[i-2] += 2*d
            if(c[i] < x):isit = False; break
        if(c[1] < x or c[0] < x):isit = False
        if(isit):l=x+1
        else:r=x-1
    print(r)