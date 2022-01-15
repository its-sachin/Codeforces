for _ in range(int(input())):
    n,m=map(int,input().split())
    def a(n,m):
        ans = n*(m//3)
        if(m%3==2):
            return ans + min(n,2*(n//3) + n%3)
        elif(m%3==0):return ans
        return ans + (n%3!=0) + (n//3)
    print(min(a(n,m),a(m,n)))