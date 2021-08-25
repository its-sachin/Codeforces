for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if(a>b):
        a,b=b,a
    
    n=2*(b-a)
    if(n<0 or n<max(a,b) or c>n):
        print(-1)
    elif(c<=n//2):
        print(c+(n//2))
    else:
        print(c-(n//2))