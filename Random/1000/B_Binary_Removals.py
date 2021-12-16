for _ in range(int(input())):
    s=input()
    z=-1
    o=-1
    for i in range(len(s)):
        if(s[i]=='1'):
            o=i
        else:
            if(z==-1):
                z=i
    if(z<o):
        print("YES")
    else:
        print("NO")