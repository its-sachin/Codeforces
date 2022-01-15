import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    even = a[0]; odd = a[1]
    for i in range(2,n,2):
        even = math.gcd(a[i],even)
        if(i+1<n):
            odd = math.gcd(a[i+1],odd)

    if(even == odd):
        print(0);continue
    
    found = True
    for i in range(0,n,2):
        if(a[i]%odd == 0):
            found = False
            break
    if(found):
        print(odd); continue
    found = True
    for i in range(1,n,2):
        if(a[i]%even == 0):
            found = False
            break
    if(found):
        print(even)
    else:
        print(0)
