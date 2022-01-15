for _ in range(int(input())):
    input()
    k,n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    i=0
    j=0
    z=0
    c=[]
    no=False
    while(i<n and j<m):
        first = False
        if(a[i]==0):
            c.append(0)
            i+=1
            z+=1
        elif(a[i]<=k+z):
            c.append(a[i])
            i+=1
        else:
            first = True

        sec = False
        if(b[j]==0):
            c.append(0)
            j+=1
            z+=1
        elif(b[j]<=k+z):
            c.append(b[j])
            j+=1
        else:
            sec=True

        if(first and sec):
            no=True
            break
    if(no):
        print(-1)
        continue   
    while(i<n):
        if(a[i]==0):
            c.append(0)
            i+=1
            z+=1
        elif(a[i]<=k+z):
            c.append(a[i])
            i+=1
        else:
            no=True
            break

    while(j<m):
        if(b[j]==0):
            c.append(0)
            j+=1
            z+=1
        elif(b[j]<=k+z):
            c.append(b[j])
            j+=1
        else:
            no=True
            break
    
    if(no):
        print(-1)
        continue  

    for i in c:
        print(i,end=" ")
    print("")


    

        