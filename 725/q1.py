import math

for _ in range(int(input())):

    n = int(input())
    array = input().split(" ")

    maxN = -1
    minN = math.inf
    maxP=-1
    minP=-1

    for i in range(n):
        if (int(array[i])>maxN):
            maxN = int(array[i])
            maxP = i
        if (int(array[i])<minN):
            minN = int(array[i])
            minP = i
    # print("ans",end=" ")
    left = min(maxP,minP)+1
    right = n-max(maxP,minP)

    if (left+right <= int(n/2)):
        print(left+right)
    else:
        print(min(max(maxP,minP)+1,left+right,n-(min(maxP,minP))))