for _ in range(int(input())):
    n=int(input())
    s=input()
    a=['a']*n

    for i in range(n):
        if(s[i]=='U'):
            a[i]='D'
        elif(s[i]=='D'):
            a[i]='U'

    i=0
    while(i<n):
        if(a[i]=='a'):
            a[i]='L'
            a[i+1]='R'
            i+=2
        else:
            i+=1

    for i in a:print(i,end='')
    print('')