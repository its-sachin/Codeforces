for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int,input().split()))
    j = len(a)-1
    count = 0
    while(count < n//2):
        print(a[j],a[0])
        count+=1
        j-=1