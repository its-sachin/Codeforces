for _ in range(int(input())):
    w,h = map(int,input().split())
    s1 = list(map(int,input().split()))[1:]
    s2 = list(map(int,input().split()))[1:]
    s3 = list(map(int,input().split()))[1:]
    s4 = list(map(int,input().split()))[1:]

    xx = [s1,s2]; yy = [s3,s4]
    x = []; y = []
    for i in range(2):
        x.append(max(xx[i]) - min(xx[i]))
        y.append(max(yy[i]) - min(yy[i]))
    print(max(max(x)*h,max(y)*w))


    




