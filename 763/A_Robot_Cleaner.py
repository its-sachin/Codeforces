for _ in range(int(input())):
    n , m, rb, cb, rd, cd = map(int,input().split())
    def ans(r,c,dr,dc,curr):
        if(r==rd or c==cd):return curr
        curr += 1
        if(r+dr > n or r+dr <1):dr=-1*dr
        if(c+dc > m or c+dc <1):dc=-1*dc
        return ans(r+dr,c+dc,dr,dc,curr)
    print(ans(rb,cb,1,1,0))
