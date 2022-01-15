p={}
i=1
while(i<=10**18):
    p[str(i)]=True
    i*=2

def f(a,b):
    i=0
    j=0
    k=0
    while(i<len(b) and j<len(a)):
        while(j<len(a) and a[j]!=b[i]):
            j+=1
        if(i<len(b) and j<len(a) and a[j]==b[i]):
            k+=1
        i+=1
        j+=1
        # print(i,j)
    return len(a)+len(b)-2*(k)
# print(f('1052','1024'))
# print(f('75','16'))

for _ in range(int(input())):
    n=(input())
    if(p.get(n)!=None):
        print(0)
        continue

    a=10**10
    for i in p:
        a=min(a,f(n,i))
        # print(a,i)
        if(a==1):
            break
    print(a)


