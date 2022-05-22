for _ in range(int(input())):
    n=int(input())
    adj={i:{} for i in range(n)}
    for i in range(n-1):
        u,v = map(int,input().split())
        adj[u-1][v-1]=i
        adj[v-1][u-1]=i
    root = -1
    for i in adj:
        if(len(adj[i])>2):root=-1;break
        elif(len(adj[i])==1):root=i
    if(root==-1):print(-1);continue
    ans = [2]*(n-1)
    for c in adj[root]:
        prev = root
        curr = c
        v = 0
        while(True):
            ans[adj[prev][curr]]+=v
            v=1-v
            if(len(adj[curr])<2):break
            for i in adj[curr]:
                if(i!=prev):
                    prev=curr
                    curr=i
                    break
    print(*ans)

    
