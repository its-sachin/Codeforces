from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    l = input().split()
    k = int(l[0])
    d={chr(i):0 for i in range(0+ord('a'),26+ord('a'))}
    for i in range(1,k+1):
        d[l[i]]=1
    for i in range(n):
        s[i]=d[s[i]]
    k = n-1; aa= [0]*n
    for i in range(n):
        if(s[n-i-1]==1):
            aa[n-i-1]=abs(i-k)
            k = i
    l = 0; ans = 0
    # print(aa)
    for i in range(n):
        # print(l,aa[i])
        if(l<=aa[i]):
            v=l
            l=0
        else:
            v=aa[i]
            l-=aa[i]
        ans = max(ans,v)
        l += 1
    print(ans)