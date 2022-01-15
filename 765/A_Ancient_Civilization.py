for _ in range(int(input())):
    n,l=map(int,input().split())
    a=list(map(int,input().split()))
    y = [0]*l
    for i in range(n):
        j=0
        while(j<l and a[i]):
            if(a[i]&1):y[j]+=1
            j+=1
            a[i]>>=1
    ans = ''; y = y[::-1]
    for i in range(l):
        if(y[i]>=n/2):ans+='1'
        else:ans+='0'

    print(int(ans,2))