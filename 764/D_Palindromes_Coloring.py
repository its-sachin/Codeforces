from typing import Counter

for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    c = Counter(s)
    double = 0
    for i in c:
        double += c[i]>>1
    def ispos(x):
        if(k*(x>>1) > double):return False
        return True
    l=1;r=n//k
    while(l<=r):
        x = (l+r)//2
        if(ispos(x)):l=x+1
        else:r=x-1
    print(r)
    
