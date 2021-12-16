MOD = 998244353
n = int(input())
a = list(map(int,input().split()))
ans = [a[0]%MOD]
for i in range(1,n):
    if(a[i] >= a[i-1]):
        ans.append((ans[-1] * ((a[i] - 1 + MOD) % MOD))%MOD)
    else:
        total = (ans[-1] * (a[i] % MOD))%MOD

        if(i == 1):
            total = (total - a[i]%MOD + MOD)%MOD
        elif(a[i-2] <= a[i]):
            total = (total - ( ans[-2]*((a[i]- 1)%MOD) )%MOD + MOD)%MOD
        else:
            

        

print(ans)
