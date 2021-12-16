for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)

    elem = {}
    for i in range(n):
        elem[a[i]] = i
    if(len(elem) != len(a)):
        print("YES")
        continue
    
    displaced = 0
    for i in range(n): 
        if(a[i] != b[i]):
            displaced = 1-displaced
            sort = elem[b[i]]
            a[i],a[sort] = a[sort],a[i]
            elem[a[i]] = i
            elem[a[sort]] = sort

    if(displaced):
        print("NO")
    else:
        print("YES")
