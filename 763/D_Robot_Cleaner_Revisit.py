mod =10**9+7;modinv = lambda x,m: pow(x,m-2,m)
for _ in range(int(input())):
    n , m, rb, cb, rd, cd, p = map(int,input().split())
    first = [0,0]; coeff = []; p = (1-(p*modinv(100,mod))%mod +mod)%mod
    r = rb; c = cb; dr = 1; dc = 1
    for i in range(4*(n-1)*(m-1)):
        if(r==rd or c==cd):coeff.append(p)
        else:coeff.append(1)
        if(r+dr > n or r+dr <1):dr=-1*dr
        if(c+dc > m or c+dc <1):dc=-1*dc
        r+=dr; c+=dc
    s = coeff[0]
    for i in range(1,len(coeff)):
        coeff[i]= (coeff[i]*coeff[i-1])%mod
        s = (s+coeff[i])%mod
    s = (s*modinv((1-coeff[-1]+mod)%mod,mod))%mod
    print(s)

    