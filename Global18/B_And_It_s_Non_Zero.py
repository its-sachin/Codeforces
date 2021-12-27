import math
for _ in range(int(input())):
    l,r = map(int,input().split())
    s = len(bin(r)[2:])
    k1 = int(math.log2(l)); k2 = math.ceil(math.log2(r+1))
    a = [2**(k2-1)]*(s)
    x = 2**(k1-1)
    for i in range(-1,-k1-1,-1):
        a[i]-=x
    for i in range(r+1,2**k2):
        k = bin(i)[2:]
        k = '0'*(s-len(k)) + k
        for j in range(len(k)):
            a[j] -= ord(k[j]) - ord('0')

    for i in range(2**k1,l):
        k = bin(i)[2:]
        k = '0'*(s-len(k)) + k
        for j in range(len(k)):
            a[j] -= ord(k[j]) - ord('0')
    a = [r-l+1-i for i in a]
    print(min(a))