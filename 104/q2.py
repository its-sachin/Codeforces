def cats(n,k) :
    b = 0
    # kd = 1
    k -=1

    if (n%2 == 0) : return (k)%n+1
    else :
        # while(kd < k) :
        #     if (k - kd >= n//2) :
        #         b = b + (n//2) + 1
        #         kd = kd + n//2
        #     else :
        #         b = b +(k-kd)
        #         kd = k
    # return b%n + 1
        return ((k+k//(n//2))%n+1)


testCases = int(input())
while (testCases > 0) :
    n,k = input().split(" ")
    print(cats(int(n),int(k)))
    testCases -= 1;
