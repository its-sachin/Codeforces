import math

def part(M,N, left, right):

    out = left-1
    pivot = M[right]
    
    i = left
    while(i < right):
        if (M[i] > pivot):
            out+= 1

            temp = M[out]
            M[out] = M[i]
            M[i] = temp

            temp = N[out]
            N[out] = N[i]
            N[i] = temp
        i +=1
    
    out += 1
    temp = M[right]
    M[right] = M[out]
    M[out] = temp

    temp = N[right]
    N[right] = N[out]
    N[out] = temp

    return out

def sortC(M,N, low, high):

    if(low<high):
        
        pivot = part(M,N,low,high)

        sortC(M,N,low,pivot-1)
        sortC(M,N,pivot+1,high)
            
for _ in range(int(input())):
    n = int(input())
    array = input().split(" ")

    gcdCount = []
    gcd = []

    for i in range(n):
        gcdCount.append(0)
        gcd.append([])

    for i in range(n):
        for j in range(i+1,n):
            gcdCurr = math.gcd(int(array[i]),int(array[j]))
            gcd[i].append(gcdCurr)
            if ( gcdCurr >1):
                gcdCount[i] += 1
                gcdCount[j] += 1

    # print(gcds,array)
    sortC(gcdCount,array,0,n-1)
    # print(gcds,array)