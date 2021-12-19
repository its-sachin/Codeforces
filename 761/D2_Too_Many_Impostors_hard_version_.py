for _ in range(int(input())):
    n = int(input())
    alls = []
    for i in range(1,n+1,3):
        print('?',i,i+1,i+2)
        alls.append(int(input()))

    i = 0
    while(i<len(alls)-1 and alls[i] == alls[i+1]): i+=1
    last = -1; a = [alls[i]]; i*=3
    for j in range(2,4):
        print('?',i+j,i+j+1,i+j+2)
        a.append(int(input()))
    a.append(alls[i//3 + 1])

    for j in range(0,len(a)-1):
        if(a[j] != a[j+1]):
            imp,crew = i+j+1, i+j+4
            if(a[j] == 1): imp,crew = crew,imp

    allimps = [imp]
    for i in range(len(alls)):

        pos = []; rej = []
        for j in range(1,4):
            k  = 3*i+j
            if(k != imp and k!= crew):pos.append(k)
            else: rej.append(k)

        if(alls[i] == 0):
            # iic iii
            if(len(pos) == 1):allimps.append(pos[0])
            elif(len(pos) == 2):
                if(rej[0] == crew):allimps.extend(pos)
                else:
                    print('?',pos[0],pos[1],crew)
                    if(int(input()) == 0):allimps.extend(pos)
                    else:
                        print('?',pos[0],imp,crew)
                        if(int(input()) == 0):allimps.append(pos[0])
                        else:allimps.append(pos[1])
            else:
                print('?',pos[0],pos[1],crew);a1 = int(input())
                print('?',pos[1],pos[2],crew);a2 = int(input())
                if(a1 == 1 and a2 == 0):pos[:] = pos[1:]
                elif(a1 == 0 and a2 == 1):pos[:] = pos[:-1]
                elif(a1 == 1 and a2 == 1):pos[:] = [pos[0],pos[-1]]
                allimps.extend(pos)
            
        else:
            if(len(pos) == 1):continue
            elif(len(pos) == 2):
                if(rej[0] == imp): continue
                else:
                    print('?',pos[0],crew,imp)
                    if(int(input()) == 0):allimps.append(pos[0])
                    else:
                        print('?',pos[1],crew,imp)
                        if(int(input()) == 0):allimps.append(pos[1])    
            else:
                print('?',pos[0],pos[1],imp);a1 = int(input())
                print('?',pos[1],pos[2],imp);a2 = int(input())
                if(a1 == 1 and a2 == 0):allimps.append(pos[2])
                elif(a1 == 0 and a2 == 1):allimps.append(pos[0])
                elif(a1 == 0 and a2 == 0):allimps.append(pos[1])

    print('!',len(allimps),*allimps)
