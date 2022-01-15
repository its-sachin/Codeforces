for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    def check(i,j,x):
        while(i<j):
            if(arr[i]!=arr[j]):
                if(x!=-1):
                    if(arr[i]!=x and arr[j]!=x):return False
                    if(arr[i]==x):i+=1
                    else:j-=1
                else:
                    return check(i+1,j,arr[i]) or check(i,j-1,arr[j])
            else:i+=1;j-=1
        return True
    print('YES' if check(0,n-1,-1) else 'NO')
            