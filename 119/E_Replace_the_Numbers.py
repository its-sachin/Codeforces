a = []; d = {}
for _ in range(int(input())):
    k = map(int,input().split())
    if(k[0] == 1):
        a.append(k[1])
    else:
        if(d.get(k[1])):
            d[k[1]]
        