import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)

def SPF(n):
    spf = [i for i in range(n+1)]
    i=2
    while(i*i<=n):
        if(spf[i]==i):
            j=i*i
            while(j<=n):
                spf[j]=i
                j+=i
        i+=1
    return spf

spf = SPF(31623)

for _ in range(II()):
    p,q = M()
    if(p%q!=0):
        P(p)
    else:
        x=p
        while(p%q!=0):
            p = p//q
        while(q!=1):
            s = spf[q]
            c=0
            while(q%s==0):
                q=q//s
                c+=1
            


        print(m)
            
