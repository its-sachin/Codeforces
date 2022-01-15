for _ in range(int(input())):
    n,a,b = map(int,input().split())

    if(a>(n-1)//2 or b>(n-1)//2 or abs(a-b)>1 or a+b > n-2):
        print(-1)
        continue

    ans = [i for i in range(1,n+1)]
    if(a<b):
        i,j = 0,1
    elif(a==b):
        i,j = 1,1
    else:
        i,j = n-1,-1

    c = 0
    while(c<max(a,b)):
        ans[i],ans[i+j] = ans[i+j],ans[i]
        i+=2*j
        c+=1

    for i in ans:
        print(i,end=' ')
    print()

