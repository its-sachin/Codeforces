def base(n,a,b):
    if(n==1):
        return True
    if((n-1)%b==0):
        return True
    return False

def f(n,a,b):
    if(n<1):
        return False
    
    if(base(n,a,b)):
        return True

    if(a!=1):
        q=a
        w=q%b
        k=n%b
        while(q<=n):
            if(w==k):
                return True
            q*=a
            w=q%b
        return False
    else:
        return False


for _ in range(int(input())):
    n,a,b = map(int,input().split())
    if(f(n,a,b)):
        print("Yes")
    else:
        print("No")