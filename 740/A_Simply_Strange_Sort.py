for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    while(True):
        c=0
        for j in range(n-1):
            if(a[j]>a[j+1]):
                c+=1
        if(c==0):
            break

        if(i%2==0):
            for j in range(0,n-1,2):
                if(a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
        else:
            for j in range(1,n-1,2):
                if(a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
        i+=1
    print(i)


        