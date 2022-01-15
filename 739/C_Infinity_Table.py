import math
for _ in range(int(input())):
    k=int(input())
    a=int(math.sqrt(k))
    if(a*a==k):
        print(a,1)
        continue
    a=a+1
    b=a-1
    if(k>=(a*a)-a+1):
        print(a,(a*a)-k+1)
    else:
        print(k-b*b,a)