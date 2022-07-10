for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(n==1):print(-1);continue
    ans=[];i=1
    while len(ans)<n:
        if(a[i-1]!=i):ans.append(i)
        else:
            if(i==n):
                l=ans.pop(-1)
                ans.append(i)
                ans.append(l)
            else:
                ans.append(i+1)
                ans.append(i)
                i+=1
        i+=1
    print(*ans)

import random
n= random.randint