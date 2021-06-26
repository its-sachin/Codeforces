import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
for _ in range(II()):
    n = II()
    aa = M()
    a = {}
    j=1
    for i in aa:
        a[j]=i
        j+=1
    c=0
    for i in range(1,n+1):
        if(a.get(i)!=0):
            k=math.ceil((2*i+1)/a.get(i))
            print("f",k,i,a.get(i))
            while(k*a.get(i)-i<=n):
                if(a.get(k*a.get(i)-i)==k):
                    c+=1
                k+=1

    print(c,"\n")