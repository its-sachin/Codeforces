for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    d={}
    for i in range(n):
        d[a[i]] = i
        
    a.sort()
    l=0
    i=0
    while(i<n):
        while(i<n-1 and d[a[i+1]]==d[a[i]]+1):
            i+=1
        i+=1
        l+=1
    if(l<=k):
        print("Yes")
    else:
        print("No")

            