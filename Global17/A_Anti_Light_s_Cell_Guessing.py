for _ in range(int(input())):
    n,m = map(int,input().split())
    if(n==m==1): print(0); continue
    print(min(2,min(n,m)))