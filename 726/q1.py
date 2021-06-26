for _ in range(int(input())):

    n = int(input())
    a = map(int, input().split())

    s = 0
    for i in a:
        s+=i
    
    if (s<n):
        print(1)
    elif (s>n):
        print(s-n)
    else:
        print(0)