for _ in range(int(input())):
    s = input()
    t = input()

    if(s==t):
        print("YES")
        continue

    d = {}
    for i in range(len(s)):
        if(s[i]==t[0]):
            d[i] = [i,0]

    if(len(d)==0):
        print("NO")
        continue

    i=1
    ss=-1
    while(i<len(t) and len(d)>0):
        for k in d.copy():
            if(d[k][1]==0):
                doo = False
                l = d[k][0]
                if(d[k][0]<len(s)-1 and s[d[k][0]+1] == t[i]):
                    d[k][0] +=1
                    d[k][1] = 1
                    doo = True
                if(l>0 and s[l-1] == t[i]):
                    if(not doo):
                        d[k][0]-=1
                        d[k][1]=-1
                    else:
                        d[ss] = [l-1,-1]
                        ss-=1
                    doo=True
                if(not doo):
                    d.__delitem__(k)
            elif(d[k][1]==1):
                doo = False
                l = d[k][0]
                if(d[k][0]<len(s)-1 and s[d[k][0]+1] == t[i]):
                    d[k][0] +=1
                    doo = True
                if(l>0 and s[l-1] == t[i]):
                    if(not doo):
                        d[k][0]-=1
                        d[k][1]=-1
                    else:
                        d[ss] = [l-1,-1]
                        ss-=1
                    doo=True
                if(not doo):
                    d.__delitem__(k)

            else:
                if(d[k][0]>0 and s[d[k][0]-1] == t[i]):
                    d[k][0]-=1
                else:
                    d.__delitem__(k)
            # print(d)

        i+=1
    
    if(len(d)>0):
        print("YES")
    else:
        print("No")
