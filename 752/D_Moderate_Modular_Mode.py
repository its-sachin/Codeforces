for _ in range(int(input())):
    x,y=map(int,input().split())
    if(y<x):print(x+y)
    elif(y%x==0):print(x)
    else:print(y- (y%x)//2)