import math
for _ in range(int(input())):
    n,h =map(int,input().split())
    a = list(map(int,input().split()))
    diff = []
    for i in range(n-1):
        diff.append(a[i+1]-a[i])
    diff.sort()

    a=0
    i=0
    done = False
    while(i<len(diff)):
        val = diff[i]
        if(a+(n-i)*val >= h):
            print(min(val,math.ceil((h-a)/(n-i))))
            done=True
            break
        c=0
        while(i<len(diff) and val==diff[i]):
            i+=1
            c+=1
        a+=val*c

    if(not done):
        print(h-a)