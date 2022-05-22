import math,sys;input=sys.stdin.readline; inf= 1e18; mod =10**9+7; pi = math.pi; e = math.e; modinv = lambda x,m: pow(x,m-2,m); import bisect; import heapq; mod9 = 998244353
for _ in range(int(input())):
    n,m = map(int,input().split())
    pos=True;inv=[];a=[]
    for p in range(n):
        arr = list(map(int,input().split()))
        sor = sorted(arr)
        my = []
        for i in range(m):
            if(arr[i]!=sor[i]):my.append(i+1)
        if(len(my)>2):pos=False  
        elif(len(my)==0):my=[1,1]     
        a.append(arr)
        inv.append(my)
        
    if(not pos):print(-1);continue
    v = [1,1]
    for i in inv:
        if(i!=[1,1]):
            if(v!=[1,1] and v!=i):pos=False;break
            v=i
    if(not pos):print(-1);continue
    elif(v==[1,1]):print(*v);continue
    for i in range(n):
        if(a[i][v[0]-1]<a[i][v[1]-1]):pos=False;break
    if(not pos):print(-1)
    else:print(*v)


