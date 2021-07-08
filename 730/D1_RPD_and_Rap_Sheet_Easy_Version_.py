import sys

for _ in range(int(input())):
    n,k = map(int,input().split())

    done =0

    ans=0
    i=0
    while(done==0):
        if(i==0):
            print(i)
        else:
            print(i^(i-1))
        done = int(input())
        sys.stdout.flush()
        i+=1

