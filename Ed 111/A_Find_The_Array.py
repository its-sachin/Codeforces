import math

def f(n):
    k= int(math.sqrt(n))
    if(k*k==n):
        return k

    else:
        return k+1

    

for _ in range(int(input())):

    s=int(input())
    print(f(s))

