for _ in range(int(input())):
    a,b=map(int,input().split())
    if(b==1):
        print("NO")
        continue
    print("YES")
    if(a==1):
        print(b,b+1,2*b+1)
    else:
        print(a*b,a,a*b+a)