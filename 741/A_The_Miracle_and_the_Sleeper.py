def f(a,b):
    k=((a)//2)+1
    if(k>=b):
        return a%k
    return a%b

def f2(a,b):
    m=a//2
    if(b>m):
        return a%b
    else:
        return a%(a//2+1)


for _ in range(int(input())):
    b,a=map(int,input().split())
    
    print(f(a,b))
