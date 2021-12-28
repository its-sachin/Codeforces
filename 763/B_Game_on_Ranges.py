for _ in range(int(input())):
    n=int(input())
    vals = {}
    ranges = []
    for i in range(n):
        l,r = map(int,input().split())
        if(vals.get(l)==None):vals[l]={'r':[r],'l':[]}
        else:vals[l]['r'].append(r)

        if(vals.get(r)==None):vals[r]={'r':[],'l':[l]}
        else:vals[r]['l'].append(l)

        ranges.append([l,r])

    for v in vals: 
        vals[v]['r'].sort()
        vals[v]['l'].sort()

    for i in ranges:
        if i[0]==i[1]:i.append(i[1])
        else:

            jr = vals[i[0]]['r'].index(i[1])
            jl = vals[i[1]]['l'].index(i[0])
            if(jl == len(vals[i[1]]['l']) -1):
                i.append(i[1])
            elif(jr == 0):
                i.append(i[0])
            else:
                i.append(vals[i[0]]['r'][jr-1]+1)

    for i in ranges:
        print(*i)
    print()

