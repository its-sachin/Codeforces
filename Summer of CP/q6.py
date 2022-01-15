n,k = map(int,input().split())

a = list(map(int,input().split()))
mod = 1000000007

st =0
count=1
prev=-1
for i in range(n):

    if (a[i]==1):
        if (st==0 and prev != -1):
            count*=(i-prev)%mod
        st+=1

    if (st==k):
        st=0
        prev=i

if (prev ==-1):
    print(0)
else:
    print(count%mod)
