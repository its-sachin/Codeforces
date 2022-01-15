for _ in range(int(input())):
    n,k=map(int,input().split())
    if(k>(n+1)//2):print(-1)
    else:
        for i in range(n):
            for j in range(n):
                x='.'
                if(i==j and (not i&1) and (i//2 <k)):x='R'
                print(x,end='')
            print()