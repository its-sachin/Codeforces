for _ in range(int(input())):
    n , m, rb, cb, rd, cd = map(int,input().split())
    def ans(a,b,x):return a-b if a>=b else 2*x - a- b
    print(min(ans(rd,rb,n),ans(cd,cb,m)))
