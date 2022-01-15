for _ in range(int(input())):
    x,n = map(int,input().split())
    m = n%4; k = 1 if x&1 else -1
    if(m == 0):print(x)
    elif(m == 1):print(x+k*n)
    elif(m == 2):print(x-k*1)
    else:print(x-(n+1)*k)