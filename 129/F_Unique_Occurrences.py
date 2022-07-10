n=int(input())
adj={i:[] for i in range(n)}
for i in range(n-1):
    u,v,k=map(int,input().split())
    adj[u-1].append([v-1,k])
    adj[v-1].append([u-1,k])
