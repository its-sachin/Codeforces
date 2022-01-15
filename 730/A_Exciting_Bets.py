import math

for _ in range(int(input())):
    a,b = map(int,input().split())
    k=abs(a-b)
    if(k==1 or k==0):
        print(k,0)
        continue
    if(a>b):
        a,b=b,a
    r = a%k
    if(r==k):
        print(k,k-r)
        continue
    print(k,min(r,k-r))

    