from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
	
    inv = [0]
    def count(l,m,r,inv):
        i = l; j = m+1
        while(i<=m and j<=r):
            if(arr[i] > 2*arr[j]):
                inv[0] += m-i+1
                j+=1
            else: i+=1

    def count1(l,m,r):
        i = l; j = m+1; c = []
        while(i<=m and j<=r):
            if(arr[i] <= arr[j]):c.append(arr[i]); i+=1
            else: 
                c.append(arr[j])
                j+=1
        while(i<=m):c.append(arr[i]);i+=1
        while(j<=r):c.append(arr[j]);j+=1
        for i in range(len(c)):
            arr[i+l] = c[i]


    def rec(l,r, inv):
        if(l<r):
            m = (l+r)//2
            rec(l,m, inv)
            rec(m+1,r, inv)
            count(l,m,r, inv)
            count1(l,m,r)
    rec(0,n-1,inv)
    return inv[0] 
    # c = 0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if(arr[i]>2*arr[j]):c+=1; print(i,j)
    # return c
# Taking inpit using fast I/O.
def takeInput() :
    # arr = [2,4,3,5,1]
    arr = [1,1,-1,-1,-1,1]
    n = len(arr)
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))