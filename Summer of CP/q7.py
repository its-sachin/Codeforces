def nc2(n):
    if (n<2):
        return 0
    return (n*(n-1))//2
    
for _ in range(int(input())):
    n = int(input())
    a = [(int(x)%8) for x in input().split()]

    e=0
    for i in a:
        if (i%2==0):
            e+=1

    c=nc2(e)+nc2(n-e)

    print(c)


