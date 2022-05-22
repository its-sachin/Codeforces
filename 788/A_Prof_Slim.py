for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    p=0
    for k in a:
        if(k<0):p+=1
    aa=[]
    i=0
    while(i<n):
        if(i<p):aa.append(-1*abs(a[i]))
        else:aa.append(abs(a[i]))
        i+=1
    print("YES" if aa == sorted(aa) else "NO")
