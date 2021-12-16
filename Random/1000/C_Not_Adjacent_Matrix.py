for _ in range(int(input())):
    n=int(input())
    if(n==1):
        print(1)
    elif(n==2):
        print(-1)
    else:

        def out(n):
            if(n==3):
                a=[
                    [2,9,7],
                    [4,6,3],
                    [1,8,5]
                ]

                return a

            else:
                a=out(n-1)
                a.append([])
                i=((n-1)**2)+1
                j=0
                done=False
                while(i<=n**2):
                    if(j>=0):
                        a[-1].append(i)
                        j+=1
                        if(j==n):
                            j=-2
                    else:
                        a[j].append(i)
                        j-=1
                    i+=2
                    if(i>n**2 and not done):
                        i=i=((n-1)**2)+2
                        done=True
                return a

        a=out(n)
        for i in range(n):
            for j in range(n):
                print(a[i][j],end=' ')
            print("")



