def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())

for _ in range(II()):
    n,x,t = M()

    l = t//x
    if (n>l):
        print((n-l-1)*l + (l*(l+1))//2)
    else:
        print((n*(n-1))//2)
