from collections import Counter
import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c=Counter(a)
    k = max(list(c.values()))
    l = math.ceil(math.log2(n/k))
    print(n-k+l)