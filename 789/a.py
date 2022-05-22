from collections import Counter
import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if(min(a)==0):print(n-a.count(0))
    else:
        c=Counter(a); k=1
        for i in c:k=max(k,c[i])
        if(k==1):print(n+1)
        else:print(n)
    
