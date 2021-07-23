for _ in range(int(input())):
    h,w = map(int,input().split())
    ans =[[0 for x in range(w)] for y in range(h)]


    c=0
    for i in range(w):
        if(c==0):
            ans[0][i] = 1
            if(h>1):
                ans[1][i]=-1
            if(i>0):
                ans[1][i-1]=-1
            if(i<w-1):
                ans[1][i+1]=-1
    
        else:
            ans[0][i]=0
        c=1-c

    c=1

    for i in range(1,h-1):
        if(c==0):
            ans[i][0]=1
        else:
            ans[i][0]=0
        c=1-c

    if(ans[1][w-1]==-1):
        c=1
    else:
        c=0

    for i in range(1,h-1):
        if(c==0):
            ans[i][w-1]=1
        else:
            ans[i][w-1]=0
        c=1-c

    c=0
    if(ans[h-2][0]==1):
        ans[h-1][0]=-1
        ans[h-1][1]=-1
        c=1
    if(ans[h-2][w-1]==1):
        ans[h-1][w-1]=-1
        ans[h-1][w-2]=-1


    for i in range(w):
        if(c==0):
            if(ans[h-1][i]!=-1):
                ans[h-1][i]=1
                c=1-c
        else:
            ans[h-1][i]=0
            c=1-c

    for i in range(h):
        for j in range(w):
            if(ans[i][j]==-1):
                print(0,end="")
            else:
                print(ans[i][j],end="")
        print("")
    print("")