for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    e=0
    for i in range(n):
        if(a[i]%2==0):
            e+=1
            a[i]=0
        else:
            a[i]=1
    o=n-e
    if(abs(e-o)>1):
        print(-1)
        continue

    a1=[]
    a2=[]
    c=0
    for i in range(n):
        a1.append(c)
        a2.append(1-c)
        c=1-c
    
    s1=0
    s2=0
    a11=[]
    a22=[]
    b11=[]
    b22=[]
    for i in range(n):

        if(a[i]!=a1[i]):
            if(a[i]==1):
                a11.append(i)

            else:
                a22.append(i)

        if(a[i]!=a2[i]):
            if(a[i]==1):
                b11.append(i)

            else:
                b22.append(i)
        # print(i1,j1)
    
    for i in range(min(len(a11),len(a22))):
        s1+=abs(a11[i]-a22[i])

    for i in range(min(len(b11),len(b22))):
        s2+=abs(b11[i]-b22[i])


    if(n%2==1):
        if(e==n//2):
            s1=max(s1,s2)
        else:
            s2=max(s1,s2)
    print(min(s1,s2))

        
    

