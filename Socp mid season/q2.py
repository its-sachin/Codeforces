mod= 10**9+7
     
t,k = map(int,input().split())
 
dp = [-1]*(100001)
ans = [-1]*(100001)
dp[0]=0
ans[0]=0
for i in range(1,k):
    dp[i]= pow(2,i,mod)
    ans[i]=(ans[i-1]+dp[i])%mod

dp[k] = (pow(2,k,mod)+pow(26,k,mod))%mod
ans[k]=(ans[k-1]+dp[k])%mod
 
done =k

for _ in range(t):
    l1,l2 = map(int,input().split())
    if(l2>done):
        for i in range(done+1,l2+1):
            if(dp[i]==-1):
                dp[i] = ((2*dp[i-1])%mod + (dp[i-k]*pow(26,k,mod))%mod)%mod
                ans[i] = (ans[i-1]+dp[i])%mod
        done = l2
    
    print((ans[l2]-ans[l1-1]+mod)%mod)