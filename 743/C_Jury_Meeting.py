mod=998244353

maxn=10**6
fact=[1]
for i in range(1,(maxn)+1):
    fact.append((fact[-1]*i)%mod)

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    
    m=max(a)
    cm=0
    cm1=0
    for i in a:
        if(i==m):
            cm+=1
        elif(i==m-1):
            cm1+=1

    if(cm==n):
        print(fact[n])
        continue

    if(cm1==0):
        print(0)
        continue

    a=cm1+cm-1

    num=(fact[n]*a)%mod
    den=pow(a+1,mod-2,mod)
    print((num*den)%mod)