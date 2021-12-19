for _ in range(int(input())):
    k,x = map(int,input().split())
    left = 1; right = 2*k-1
    while(left<right):
        mid = (left+right)//2
        if(mid<=k):
            val = mid*(mid+1)//2
        else:
            val = k*(k+1)//2 + (mid-k)*(3*k - mid - 1)//2
            
        if(val<x):left = mid+1
        elif(val>x):right = mid 
        else:break
    print((left+right)//2)