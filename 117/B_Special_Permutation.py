for _ in range(int(input())):
    n,a,b = map(int,input().split())
    if(a==n//2+1 and b ==n//2):
        ans = [i+1 for i in range(n)][::-1]
        print(*ans); continue
    elif(a>=n//2+1 or b<=n//2): print(-1); continue
    aa,bb =[a],[b]
    for i in range(b+1,n+1):aa.append(i)
    for i in range(1,a):bb.append(i)
    i = a+1
    while(len(aa)!=n//2):
        aa.append(i)
        i+=1
    while(len(bb)!=n//2):
        bb.append(i)
        i+=1
    
    aa.extend(bb)
    print(*aa)