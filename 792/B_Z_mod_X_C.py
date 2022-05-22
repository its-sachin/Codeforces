for _ in range(int(input())):
    a,b,c = map(int,input().split())
    x,y,z = a+b+c,b+c,c
    print(x,y,z)
    # print(x%y==a,y%z==b,z%x==c)
