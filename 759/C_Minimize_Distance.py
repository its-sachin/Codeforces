def anss(a,k):
    ans = 0
    n = len(a)
    curr = 0

    while curr!=n-1:
        if(curr == 0):
            next = curr + (n-1)%k
            if(next == 0):
                next = curr + k
        else:
            next = curr + k

        if next >= n-1:
            ans += a[-1]
            curr = n-1
        else:
            ans += 2*a[next]
            curr = next
    return ans

for _ in range(int(input())):
    n,k = map(int,input().split())
    b = list(map(int,input().split()))
    pos = [0]
    neg = [0]
    for i in b:
        if(i>0):
            pos.append(i)
        elif(i<0):
            neg.append(-1*i)
    pos.sort()
    neg.sort()
    ansPos = anss(pos,k)
    ansNeg = anss(neg,k)
    if(len(pos)==1 or len(neg) == 1):
        print(ansPos + ansNeg)
        continue
    else:
        print(ansNeg +ansPos + min(pos[-1],neg[-1]))


