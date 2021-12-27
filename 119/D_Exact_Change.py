for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c2,c1,c3 =-1,-1,-1
    for i in a:
        if(i%3==2): c2 = max(c2,i) 
        elif(i%3==1): c1 = max(c1,i) 
        else: c3 = max(c3,i)
    cm = max(c1,c2,c3)

    