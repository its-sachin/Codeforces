for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(n<=2):print(0);continue
    ans = n
    for i in range(n):
        for j in range(i+1,n):
            diff = a[j]-a[i]
            coeff = j-i;c=0
            for k in range(n):
                if(coeff*a[k] != coeff*a[i] + diff*(k-i)):c+=1
            ans=min(ans,c)
    print(ans)
    