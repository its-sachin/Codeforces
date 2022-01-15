for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    h = 1
    for i in range(n):
        if(a[i] == 1):
            if(i == 0):
                h+=1
            else:
                if(a[i-1]==1):
                    h+=5
                else:
                    h+=1
        else:
            if(i!=0 and a[i-1]==0):
                h=-1
                break
    print(h)