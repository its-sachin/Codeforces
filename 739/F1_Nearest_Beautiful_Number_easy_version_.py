def numd(n):
    d={}
    p=0
    for i in n:
        d[i]=True
        p+=1
    return len(d),p

for _ in range(int(input())):
    n,k = map(int,input().split())
    nst=str(n)
    dist,l=numd(nst)

    first = nst[0]
    i=0
    while(i<l and nst[i]==first):
        i+=1
    if(i>=l or nst[i]<first):
        if(k==2):
            if(dist==2):
                print(min(first*l,nst))
                continue
            elif(i==l):
                print(first*l)
                continue
                
        else:
            print(first*l)
            continue

    if(k==1):
        print(str(int(first)+1)*l)
    elif(dist==2):
        print(nst)
    else:
        k=i
        c=0
        second = nst[i]
        while(i<l and nst[i]==first or nst[i]==second):
            if(nst[i]==second):
                c+=1
            i+=1
        if((c==1) and second<first):
            print(nst[:k]+first+('0'*(l-k-1)))
        elif(first>second):
            first,second=second,first

        elif(nst[i]<first):
            print(nst[:i]+first*(l-i))
        elif(nst[i]<second):
            print(nst[:i]+second+first*(l-i-1))
        else:
            if(nst[0]==first):
                a=''
                done=False
                for j in range(i):
                    if(nst[j]==second and not done):
                        a+=str(int(second)+1)
                        done=True
                    else:
                        a+=first
                b=nst[:i]
                j=i-1
                while(b[j]==second):
                    j-=1
                b=b[:j]+second+first*(l-j-1)
                a+=(first)*(l-i)
                print(min(a,b))
            else:
                a=[j for j in nst[:i]]
                i=0
                while(i<len(a) and a[len(a)-i-1]==second):
                    a[len(a)-i-1]=first
                    i+=1
                a[len(a)-i-1]=second
                while(len(a)<l):
                        a+=first
                s=''
                for i in a:
                    s+=i
                print(s)




