for _ in range(int(input())):
    a,s = input().split()
    b = ''
    j = len(s)-1; got  = True
    for i in range(len(a)-1,-1,-1):
        if(j<0):got = False; break
        if(int(a[i]) <= int(s[j])):
            b += str(int(s[j]) - int(a[i]))
            j -= 1
        else:
            if(j<1):got = False; break
            c = int(s[j-1] + s[j])
            if(int(a[i]) + 9 < c or c < int(a[i])):got = False; break
            b += str(c - int(a[i]))
            j -= 2
    print(int(s[:j+1] + b[::-1]) if got else -1)