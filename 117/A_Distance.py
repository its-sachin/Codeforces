for _ in range(int(input())):
    x,y = map(int,input().split())
    a,b = 0,(x+y)//2
    if(x>y): a,b = b,a
    print(-1,-1) if (x-y)%2 else print(a,b)
