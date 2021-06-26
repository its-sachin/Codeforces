def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())
def P(a):
    print(a)
for _ in range(II()):
    p,q = M()
    while(p%q==0):
        p=p//q
    P(p)