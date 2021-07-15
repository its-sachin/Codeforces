for _ in range(int(input())):
    input()
    xa,ya = map(int,input().split())
    xb,yb = map(int,input().split())
    xf,yf = map(int,input().split())

    ans = abs(xa-xb)+abs(ya-yb)
    if((xa==xb and xa==xf and yf<max(ya,yb) and yf>min(ya,yb)) or (ya==yb and ya==yf and xf<max(xa,xb) and xf>min(xa,xb))):
        ans+=2
    print(ans)
        