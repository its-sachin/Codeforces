n,q = map(int,input().split())
s = input()

d = {'a':{},'b':{},'c':{}}
for i in range(n):
    d[s[i]][i] = True

lens = {i:len(d[i]) for i in d}
abc = {}
for i in d['a']:
    if(d['b'].get(i+1) and d['c'].get(i+2)):
        abc[i] = True
count = len(abc)

for i in range(q):
    pos,c = input().split()
    pos=int(pos)-1

    if(d[c].get(pos) == None):
        for i in lens:
            if(i != c and d[i].get(pos)):
                d[i][pos] = None
                lens[i]-=1
        d[c][pos] = True
        lens[c]+=1

        rng = {'a':[pos-1,pos-2],'b':[pos,pos-2],'c':[pos,pos-1]}
        for i in range(2):
            if(abc.get(rng[c][i])):
                abc[rng[c][i]] = None
                count -=1
        
        if(c=='a' and d['b'].get(pos+1) and d['c'].get(pos+2)):
            abc[pos] = True
            count+=1
        elif(c=='b' and d['a'].get(pos-1) and d['c'].get(pos+1)):
            abc[pos-1] = True
            count+=1
        elif(c=='c' and d['a'].get(pos-2) and d['b'].get(pos-1)):
            abc[pos-2] = True
            count+=1
    
    print(count)

