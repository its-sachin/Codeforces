import math

testCases = int(input())
while (testCases > 0) :
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    ans  = 0
    for i in range (1,n) :
        if(a[i] >= a[i-1]) :
            m = a[i-1]
            M = a[i]
        else :
            M = a[i-1]
            m = a[i]

        if (M > 2*m) :
            while(M> 2*m):
                m = 2*m
                ans += 1

    print(ans)
    testCases -= 1;
