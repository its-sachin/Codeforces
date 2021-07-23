for _ in range(int(input())):
    s = input()
    
    wa=0
    wb=0
    qa=0
    qb=0
    k=0
    pl = 0
    done = False
    t = len(s)
    while(not done and k<t):
        if(pl==0):
            if(s[k]=='1'):
                wa+=1
            elif(s[k]=='?'):
                qa+=1
        else:
            if(s[k]=='1'):
                wb+=1
            elif(s[k]=='?'):
                qb+=1
        pl=1-pl
        k+=1
        if(wa+((t-k)//2)<wb+qb or wb+((t-k+1)//2)<wa+qa):
            print(k)
            done = True
    if(not done):
        print(k)
