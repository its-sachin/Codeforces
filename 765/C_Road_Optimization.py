# n,l,k=map(int,input().split())
# d=list(map(int,input().split()))
# d.append(l)
# for i in range(n,0,-1):d[i] = d[i]-d[i-1]
# d = d[1:]
# a=list(map(int,input().split()))

# dp = [[[0,0] for i in range(k+1)] for j in range(n+1)]
# for i in range(1,n+1):
#     dp[i][0] = [a[i-1]*d[i-1] + dp[i-1][0][0],a[i-1]]
# for i in range(1,k+1):
#     dp[1][i] = [dp[1][0][0],a[0]]

# for i in range(2,n+1):
#     for j in range(1,k+1):
#         v1 = dp[i-1][j-1][0] + dp[i-1][j-1][1]*d[i-1]
#         v2 = dp[i-1][j][0]+a[i-1]*d[i-1]
#         if(v1<=v2):dp[i][j] = [v1,dp[i-1][j-1][1]]
#         else:dp[i][j] = [v2,a[i-1]]

# print(min(dp[-1])[0])
def a1(n,l,k,A,D):
    D.append(l)
    DP=[[1<<60]*(k+1) for i in range(n+1)]
    DP[0][0]=0
    
    for i in range(n):
        a=A[i]
        for j in range(k+1):
            for to in range(i+1,n+1):
                if j+to-i-1<=k:
                    DP[to][j+to-i-1]=min(DP[to][j+to-i-1],DP[i][j]+a*(D[to]-D[i]))
    
    return min(DP[-1])



def a2(n,l,k,a,d):
    d.append(l)
    for i in range(n,0,-1):d[i] = d[i]-d[i-1]
    d = d[1:]

    dp = [[[0,0] for i in range(k+1)] for j in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = [a[i-1]*d[i-1] + dp[i-1][0][0],a[i-1]]
    for i in range(1,k+1):
        dp[1][i] = [dp[1][0][0],a[0]]

    for i in range(2,n+1):
        for j in range(1,k+1):
            v1 = dp[i-1][j-1][0] + dp[i-1][j-1][1]*d[i-1]
            v2 = dp[i-1][j][0]+a[i-1]*d[i-1]
            if(v1<=v2):dp[i][j] = [v1,dp[i-1][j-1][1]]
            else:dp[i][j] = [v2,a[i-1]]
    return min(dp[-1])[0]

import random

while True:
    n = random.randint(2,5)
    k = random.randint(1,5)
    l = random.randint(1,100)
    a,d=[],[]
    for i in range(n-1):
        a.append(random.randint(1,10))
        d.append(random.randint(1,l))
    d.append(0)
    d.sort()
    a.append(random.randint(1,10))

    print(n,l,k)
    print(d)
    print(a)
    aa1=a1(n,l,k,a,d)
    aa2=a2(n,l,k,a[:],d[:])

    if(aa1!=aa2):print(aa1,aa2);break
