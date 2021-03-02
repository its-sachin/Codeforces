def cons(n,u,r,d,l):
    if (u == n):
        if (r==0 or l==0): return "no"
        else:
            r-=1
            l-=1
            if (d<= n-2): return "yes"
            else:
                if (d ==n):
                    if (r==0 or l==0): return "no"
                    else: return "yes"
                else:
                    if (r==0 and l==0): return "no"
                    else: return "yes"

    else:
        if (r==0 and l==0): return "no"
        else:
            if (r>=l) :
                r-=1
            else: l-=1

            if (d<= n-2): return "yes"
            else:
                if (d ==n):
                    if (r==0 or l==0): return "no"
                    else: return "yes"
                else:
                    if (r==0 and l==0): return "no"
                    else: return "yes"

def out(n,u,r,d,l) :
    if (u>n or l>n or r>n or d>n):
        return "no"
    else:
        if (u<=n-2 and r<=n-2 and d<=n-2 and l<=n-2):
            return "yes"
        else:
            if (u > n-2):
                return cons(n,u,r,d,l)
            elif (r>n-2):
                return cons(n,r,d,l,u)
            elif (d>n-2):
                return cons(n,d,l,u,r)
            else: return cons(n,l,u,r,d)



num = int(input())


while(num>0):

    n,u,r,d,l = input().split(" ")
    n = int(n)
    u = int(u)
    l = int(l)
    d = int(d)
    r = int(r)

    print(out(n,u,r,d,l))

    num -=1