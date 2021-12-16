for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    
    if(n==1):
        print('YES\n'+str(b[0])) if b[0]>0 else print('NO')
        continue

    DET = n*(n+1)
    inv = [-1*(DET-2),DET+2]
    DET*= n
    s = 2*sum(b)
    valid  = True
    ans = []
    for i in range(n):
        curr = s + (b[(i-1)%n]*(inv[-1]-2)) + (b[i]*(inv[0]-2))
        if(curr <=0 or curr % DET != 0):
            valid = False
            break
        ans.append(curr//DET)
    if(valid):
        print('YES')
        for i in range(n): print(ans[i],end=' ')
        print()
    else:
        print('NO')