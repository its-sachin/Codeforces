for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    like = []; dislike = []
    s=input()
    for i in range(n):
        if(s[i]=='1'):
            like.append([a[i],i])
        else:
            dislike.append([a[i],i])
    like.sort(reverse=True)
    dislike.sort()

    r=1
    for i in dislike:   
        a[i[1]]=r
        r+=1
    r=n
    for i in like:
        a[i[1]]=r
        r-=1
    print(*a)