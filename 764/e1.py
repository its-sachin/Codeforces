mod =10**9+7
for _ in range(int(input())):
    input()
    n,m=map(int,input().split())
    nums=[]
    for i in range(n):nums.append(input())
    s=input()
 
    p = 69
    powers = [1]
    for i in range(m):
        powers.append((powers[-1]*p)%mod)
 
    def hash(a):
        h = 0; n = len(a)
        for i in range(n):
            h = (h + (ord(a[i])*powers[n-i])%mod)%mod
        return h
 
    def issubstr(a,b):
        h1 = hash(a);n=len(a); h2 = hash(b[:n])
        for i in range(n,len(b)+1):
            if(h1==h2):
                return i-len(a)
            if(i>=len(b)):break
            h2 = (((h2 + ord(b[i]) - (ord(b[i-n])*powers[n])%mod)%mod)*p)%mod
        return -1
 
    def ans(a):
        if(len(a)<2):return
        for i in range(n):
            curr = issubstr(a,nums[i])
            if(curr!=-1):return [[curr+1,curr+len(a),i+1]]
        if(len(a)>=4):
            for i in range(2,len(a)-1):
                s1 = ans(a[:i])
                s2 = ans(a[i:])
                if(s1!=None and s2!=None):return s1+s2
 
    a = ans(s)
    if(a==None):print(-1)
    else:
        print(len(a))
        for i in a:
            print(i[0],i[1],i[2])