for _ in range(int(input())):
    s = input()
    f=-1
    for i in range(len(s)):
        if(s[i]=='a'):
            f=i
            break
    if(f==-1):
        print("NO")
        continue
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    done=1
    r=f+1
    l=f-1
    no=False
    while((r<len(s) or l>=0) and not no):
        if(r<len(s) and s[r]==arr[done]):
            r+=1
            done+=1
        elif(l>=0 and s[l]==arr[done]):
            l-=1
            done+=1
        else:
            print("NO")
            no=True
    if(not no):
        print("YES")