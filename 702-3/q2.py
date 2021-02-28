
testCases = int(input())
while (testCases > 0) :
    n = int(input())
    ar = [int(x) for x in input().split(" ")]

    a = 0
    b = 0
    c = 0
    for i in range(n):
        if (ar[i]%3 == 0): a +=1
        elif (ar[i]%3 == 1): b +=1
        else: c +=1

    out = 0
    while (a!=b or b !=c) :
        if (a>=b and a>=c) :
            a-=1
            b+=1
            out += 1
        elif(b>=c and b>=a):
            b-=1
            c+=1
            out +=1
        elif(c>=a and c>=b):
            c-=1
            a+=1
            out +=1
        # print(a,b,c)


    print(out)
    testCases -= 1;
