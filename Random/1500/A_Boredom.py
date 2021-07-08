n = int(input())
a = list(map(int,input().split()))

dp = [0]*100001
curr,prev=0,0
for i in a:
    dp[i]+=i
for i in dp:
    curr,prev = max(curr,prev+i),curr

print(curr)
