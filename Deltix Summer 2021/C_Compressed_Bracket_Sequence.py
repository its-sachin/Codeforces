import numpy as np

arrSize = 51
n=int(input())
a=list(map(int,input().split()))

for i in range(1,n,2):
    a[i]=-1*a[i]
s=0
maxsum=0
for i in a:
    s+=i
    if(s<0):
        s=0
    maxsum=max(s,maxsum)

dp = np.zeros((arrSize, maxsum));
visit = np.zeros((arrSize, maxsum));

def SubsetCnt(i, s, arr, n) :
     
    # Base cases
    if (i == n) :
        if (s == 0) :
            return 1;
        else :
            return 0;
     
    # Returns the value
    # if a state is already solved
    if (visit[i][s + arrSize]) :
        return dp[i][s + arrSize];
 
    # If the state is not visited,
    # then continue
    visit[i][s + arrSize] = 1;
 
    # Recurrence relation
    dp[i][s + arrSize ] = (SubsetCnt(i + 1, s + arr[i], arr, n) +
                           SubsetCnt(i + 1, s, arr, n));
 
    # Returning the value
    return dp[i][s + arrSize];

print(SubsetCnt(0,0,a,n))