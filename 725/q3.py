import math

def part(M, left, right):

    out = left-1
    pivot = M[right]
    
    i = left
    while(i < right):
        if (M[i] < pivot):
            out+= 1

            temp = M[out]
            M[out] = M[i]
            M[i] = temp
        i +=1
    
    out += 1
    temp = M[right]
    M[right] = M[out]
    M[out] = temp

    return out

def sortC(M, low, high):

    if(low<high):
        
        pivot = part(M,low,high)

        sortC(M,low,pivot-1)
        sortC(M,pivot+1,high)

def lt(a,left,right,ub):

    if (a[left] >ub):
        return (-1,0)
    else:
        low = left
        while(left<=right):
            mid = (left+right)//2

            if (a[mid] < ub):
                left = mid+1
                

            elif (a[mid] > ub):
                right = mid-1

            else:
                if ((mid==len(a)-1) or (a[mid+1]>ub)):
                    right=mid
                    break
                else:
                    left = mid+1

            
        high = right

        return (low,high)

def lgt(a,left,right,ub,lb):

    # print("finding less than",ub)

    (low,high) = lt(a,left,right,ub)

    # print(low,high)

    if (low==-1):
        return 0

    # print("finding less than",lb)

    (low1,high1) = lt(a,low,high,lb)

    # print(low1,high1)

    if (low1==-1):
        return (high-low+1)

    else:
        n = (high-low+1)
        if (a[high1] == lb):
            c=n-(high1-low1)
        else:
            c=n-(high1-low1+1)
        return c


for _ in range(int(input())):

    n,l,r = input().split(" ")
    n,l,r = int(n),int(l),int(r)
    a = [int(x) for x in input().split(" ")]

    c = 0
    k = 0
    sortC(a,0,n-1)
    # print(a)

    for i in a:
        if (i>r):
            continue

        t = lgt(a,0,n-1,r-i,max(l-i,0))
        c+= t
        # print("between them ",t)
        if (c<=r-i and c>=l-i):
            k+=1

    # print("a",end=" ")
    print(max(int((c-k)/2),0))

    # print("")