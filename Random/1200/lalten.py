def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())
# for _ in range(II())

n,l = M()
a = L()
a.sort()
m = max(a[0],l-a[n-1])
for i in range(1,n):
    k = (a[i]-a[i-1])/2
    if (k>m):
        m=k

print(m)
