inf = 10**18
for _ in range(int(input())):
    input()
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    t = list(map(int,input().split()))
    arr = []
    for i in range(k):
        arr.append([a[i],t[i]])
    arr.sort()
    m = [inf]*n
    m[arr[0][0]-1] = arr[0][1]
    lastM = 0
    lastA = 0
    for i in range(arr[0][0],n):
        if(lastA<k-1 and i==arr[lastA+1][0]-1):
            lastA+=1
            if(arr[lastA][1]<arr[lastM][1]+(i-arr[lastM][0]+1)):
                lastM=lastA
        m[i] = arr[lastM][1]+(i-arr[lastM][0]+1)

    m[arr[k-1][0]-1] = min(m[arr[k-1][0]-1],arr[k-1][1])
    lastM=k-1
    lastA=k-1
    for i in range(arr[k-1][0]-1,-1,-1):
        if(lastA>0 and i==arr[lastA-1][0]-1):
    
            lastA-=1
            if(arr[lastA][1]<arr[lastM][1]+(arr[lastM][0]-i-1)):
                lastM=lastA
        m[i] = min(m[i],arr[lastM][1]+(arr[lastM][0]-i-1))

    for i in m:
        print(i,end=" ")
    print("")
