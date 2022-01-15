for _ in range(int(input())):
    s = input()
    t = input()

    n = len(s)
    m = len(t)

    if(m>n):
        print("NO")
        continue

    if(t=="" or s==t):
        print("YES")
        continue

    i=n-1
    j=m-1
    while(i>=0 and j>=0):
        if(s[i]==t[j]):
            i-=1
            j-=1
        else:
            i-=2
    if(j<0):
        print("YES")
    else:
        print("NO")
