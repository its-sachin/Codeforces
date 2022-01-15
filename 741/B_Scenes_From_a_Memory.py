np={1:True,4:True,6:True,8:True,9:True}
for _ in range(int(input())):
    k=int(input())
    n=input()
    d={}
    done=False
    # print('\n')
    j=0
    for i in n:
        if(np.get(int(i))==True):
            print(1)
            print(i)
            done=True
            break

    if(done):
        continue
    for i in n:

        if(d.get(i)!=None):
            print(2)
            print(i*2)
            done=True
            break
        else:
            d[i]=j
        j+=1

    if(done):
        continue

    if(d.get('5') !=None):
        i='5'
        for j in d:
            if(d[j]<d[i]):
                i=j+i
                done=True
                break

    if(done):
        print(2)
        print(i)
        continue

    if(d.get('2') !=None):
        i='2'
        for j in d:
            if(d[j]<d[i]):
                i=j+i
                done=True
                break
        

    if(done):
        print(2)
        print(i)
        continue

    if(d.get('5')!=None and d.get('7')!=None):
        print(2)
        print(57)
        continue

    print(2)
    print(27)



