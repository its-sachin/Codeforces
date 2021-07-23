for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
 
    val={}
    nd = {i+1:True for i in range(n)}
    na = {i+1:True for i in range(n)}
    ans = [0]*n
    for i in range(n):
        if(val.get(a[i])==None):
            val[a[i]]=i+1
            nd.pop(i+1)
            na.pop(a[i])
            ans[i]=a[i]
 
    # print(ans,nd,na,val)
    print(n-len(na))
    for i in nd:
        done =False
        for j in na:
            if(j!=i):
                ans[i-1]=j
                na.pop(j)
                done =True
                break
        if(not done):
            if(len(nd)!=1):
                for k in nd:
                    if(i!=k):
                        ans[i-1]=ans[k-1]
                        ans[k-1]=i
                        break
            else:
                ans[i-1]=a[i-1]
                ans[val[a[i-1]]-1]=i
 
    for i in ans:
        print(i,end=" ")
    print("")