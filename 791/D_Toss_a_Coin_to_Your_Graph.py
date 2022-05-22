import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n,m1,k=M();a=L();adj=[[] for i in range(n)];k-=1
for i in range(m1):u,v=M();adj[u-1].append(v-1)
l=0;r=1000000000;ans=-1
while l<=r:
    m=(l+r)//2;cyc=[0];dp=[-1]*n;c=[0]*n
    def dfs(r):
        c[r]=1;dp[r]=0
        for j in adj[r]:
            if a[j]>m:continue
            if c[j]==1:cyc[0]=1
            elif c[j]==0:dfs(j)
            dp[r]=max(dp[r],1+dp[j])
        c[r]=2
    for i in range(n):
        if a[i]<=m:dfs(i)
    if cyc[0] or max(dp)>=k:ans=m;r=m-1
    else:l=m+1
print(ans)