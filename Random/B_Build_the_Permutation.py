for _ in range(int(input())):
    n,a,b = map(int,input().split())
    
    if(abs(a-b)>1 or n<a+b+2):
        print(-1); continue
        
    ans = [i+1 for i in range(n)]
    k=0
    if(a>b):ans=ans[::-1]
    elif(a==b):k=1
    for i in range(max(a,b)):
        ans[k],ans[k+1]=ans[k+1],ans[k]
        k+=2
    print(*ans)