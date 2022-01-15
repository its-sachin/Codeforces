for _ in range(int(input())):
    n=int(input())
    s=input()
    done=False
    for i in range(1,n):
        if(s[i]!=s[i-1]):
            print(i,i+1)
            done=True
            break
    if(not done):
        print(-1,-1)
            