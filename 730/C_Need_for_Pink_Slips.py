zero = 0.000001

def f(c,m,p,v,i,prob):

    if(1-p<=zero):
        return 0
    a1=0
    c1=c
    m1=m
    p1=p
    prob1 = prob
    if(c>zero):
        o = min(c,v)
        if(m>zero):
            m,p=m+o/2,p+o/2
        else:
            p=p+o
        prob = prob*c
        a1 = i*prob*p+ f(c-o,m,p,v,i+1,prob)
        # print(i,prob*p)
    a2=0
    if(m>zero):
        t = min(m1,v)
        if(c1>zero):
            c1,p1=c1+t/2,p1+t/2
        else:
            p1=p1+t
        prob1 = prob1*m1
        a2 =i*prob1*p1 +f(c1,m1-t,p1,v,i+1,prob1)
        # print(i,prob1*p1)
    return a1+a2


for _ in range(int(input())):
    c,m,p,v = map(float,input().split())
    print(f(c,m,p,v,2,1)+p)