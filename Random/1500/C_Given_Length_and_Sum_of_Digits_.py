m,s = map(int,input().split())
if((s==0 and m>1) or s>9*(m)):
    print("-1 -1")
else:
    small,large = 0,0
    s,l=s,s
    i=1
    while(i<=m):
        if(s-9*(m-i) > 9):
            small=-1
            break

        if(s==0):
            small=10*small
        elif(s-9*(m-i)<0):
            if(small==0):
                small=1
                s-=1
            else:
                small=10*small
        else:
            small = 10*small + s-9*(m-i)
            s=9*(m-i)
        i+=1
    i=1
    while(i<=m):
        if(l>=9):
            large=large*10+9
            l-=9
        elif(l>0):
            large = large*10+l
            l=0
        else:
            large=10*large
        i+=1

    print(small,large)
