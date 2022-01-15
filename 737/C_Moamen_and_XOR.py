mod=10**9+7
def modDivide(a,b,m):
    inv = pow(b, m - 2, m)
    return (inv*a) % m


for _ in range(int(input())):
    n,k = map(int,input().split())
    if(k==0):
        print(1)
        continue
        
    if(n%2==1):
        print(pow(1+pow(2,n-1,mod),k,mod))
    else:
        t = pow(pow(2,n-1,mod)-1,k,mod)
        a = pow(2,n*k,mod)
        b = (pow(2,n-1,mod)+1)%mod
        a = modDivide((a-t+mod)%mod,b,mod)
        t=(t+a)%mod
        print(t)
