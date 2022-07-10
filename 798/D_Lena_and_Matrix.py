for _ in range(int(input())):
    n,m = map(int,input().split())
    b=[]
    for i in range(n):
        s=input()
        for j in range(m):
            if(s[j]=='B'):b.append([i,j])
    