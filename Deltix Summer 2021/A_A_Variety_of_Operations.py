for _ in range(int(input())):
    c,d=map(int,input().split())
    if(c==0 and d==0):
        print(0)
    elif(c==d):
        print(1)
    elif((c+d)%2==0):
        print(2)
    else:
        print(-1)