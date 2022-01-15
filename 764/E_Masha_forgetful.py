mod =10**9+7
for _ in range(int(input())):
    input()
    n,m=map(int,input().split())
    nums=[]
    for i in range(n):nums.append(input())
    s=input()

    p = 69
    powers = [1]
    for i in range(m):
        powers.append((powers[-1]*p)%mod)

    def hash(a):
        h = 0; n = len(a)
        for i in range(n):
            h = (h + (ord(a[i])*powers[n-i])%mod)%mod
        return h

    def issubstr(a,b):
        h1 = hash(a);n=len(a); h2 = hash(b[:n])
        for i in range(n,len(b)+1):
            if(h1==h2):
                return i-len(a)
            if(i>=len(b)):break
            h2 = (((h2 + ord(b[i]) - (ord(b[i-n])*powers[n])%mod)%mod)*p)%mod
        return -1

    dp = [[-1,-1] for i in range(m)]
    for i in range(m-1):
        def sett(a,v,l):
            for j in range(n):
                k = issubstr(a,nums[j]) 
                if(k!=-1):dp[v][l]=(k+1,j+1);break
        a = s[i]+s[i+1]
        sett(a,i,0)
        if(i<m-2):sett(a+s[i+2],i,1)

    i=0
    ans = []; valid = True
    while(i<m):
        if(dp[i][0]==-1 and dp[i][1]==-1):valid=False;break
        elif(dp[i][1]!=-1):
            l,v = dp[i][1]
            ans.append([l,l+2,v])
            i+=3
        else:
            l,v = dp[i][0]
            ans.append([l,l+1,v])
            i+=2
            
    if(valid):
        # print(len(ans))
        # for i in ans:print(*i)
        print(1)
    else:print(-1)