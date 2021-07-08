for _ in range(int(input())):
    n= int(input())
    a = list(map(int,input().split()))
    s=0
    z=0
    for i in a:
        s+=i
        if(i==0):
            z+=1
    if(s>=n):
        if(s//n==s/n):
            print(0)
            continue
        else:
            k = s//n
            d = s-(k*n)
            print(d*(n-d))
            continue

    else:
        if(z==n):
            print(0)
            continue
        if(s//(n-z)==s/(n-z)):
            print((s*z))
            continue
        else:
            k=s//(n-z)
            d = s-(k*(n-z))
            print(d*(n-z-d)+(k+1)*d*z+k*z*(n-z-d))

