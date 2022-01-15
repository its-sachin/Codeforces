MOD = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    plus1 = [0]*(n+2)
    minus1 = [0]*(n+2)
    plus1[0] = 1

    for i in a:
        plus1[i+1] = ((2*plus1[i+1])%MOD + plus1[i])%MOD
        if(i>0):
            minus1[i-1] = ((2*minus1[i-1])%MOD + plus1[i-1])%MOD
        minus1[i+1] = (2*minus1[i+1])%MOD

    print(plus1,'\n',minus1)
    print(((sum(plus1) + sum(minus1))%MOD - 1 + MOD)%MOD)