import math
for _ in range(int(input())):
    a = int(input())
    if(a%2==0):
        print(2,a-3,1)
    else:
        if(a%3!=1):
            print(3,a-4,1)
        else:
            n = a-1
            for i in range(5,n+1,2):
                if(math.gcd(i,n-i)==1):
                    print(i,n-i,1)
                    break