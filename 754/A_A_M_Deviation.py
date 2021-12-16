for _ in range(int(input())):
    a,b,c = map(int,input().split())
    print(0) if (a+b+c)%3==0 else print(1)