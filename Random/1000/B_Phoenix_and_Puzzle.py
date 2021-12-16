import math
for _ in range(int(input())):
    n=int(input())
    if(int(math.sqrt(n/2))**2==n/2 or int(math.sqrt(n/4))**2==(n/4)):
        print("YES")
    else:
        print("NO")