def numTaken(n,k):
    return (n+k)-(n+k)//4

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()
    c=a[0:]

    for i in range(n-2,-1,-1):
        a[i]+=a[i+1]
        b[i]+=b[i+1]

    k=0
    nm =numTaken(n,k)
    i=n-nm
    s1 = a[n-nm]
    s2 = b[n-nm]

    # print(s1,s2,nm,i)
    while(s2>s1):
        k+=1
        nm1=numTaken(n,k) 
        diff = nm1-nm
        if(nm1<=n):
            s2=b[n-nm1]

        if(diff==0):
            if(i<n):   
                s1-=c[i]
                i+=1
            else:
                s1-=100
        s1+=100
        nm=nm1

        # print(s1,s2,nm,i)
    print(k)