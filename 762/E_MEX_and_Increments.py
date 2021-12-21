import bisect
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    count = {}
    for i in a:
        if(count.get(i)): count[i] += 1
        else: count[i] = 1
    make = [count.get(0,0)]
    small = make[-1]
    left = []
    if(small > 1):
        left.append([0,small-1])
    for i in range(1,n+1):
        if(small < i):
            make.extend([-1]*(n-i+1)); break
        elif(count.get(i-1)):
            make.append(make[-1]-count[i-1]+count.get(i,0))
        else:
            make.append(make[-1] + count.get(i,0) + i - 1 -left[-1][0])
            left[-1][1]-=1
            if(left[-1][1]==0):left.pop()
        k =  count.get(i,0)
        if(k > 1):
            left.append([i,k-1])
        small += k
    print(*make)




