def toprint(n) :
    if (n%2 ==1) :
        curr1 = True
        for i in range (n*(n-1)//2) :
            if (curr1) :
                print(1, end = " ")
                curr1 = False
            else :
                print(-1, end  =" ")
                curr1 = True

    else :
        curr1 = True
        done0 = True
        j = 0
        k = 1
        for i in range (n*(n-1)//2) :

            if (j == n-k) :
                curr1 = not curr1
                if(k%2 == 0) : done0 = True
                k += 1 
                j = 0

            if (done0) :
                print(0, end = " ")
                done0 = False
            elif (curr1) :
                print(1, end = " ")
                curr1 = False
            else :
                print(-1, end  =" ")
                curr1 = True
            j +=1



testCases = int(input())
while (testCases > 0) :
    n = int(input())
    toprint(n)
    testCases -= 1;
