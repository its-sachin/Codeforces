def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())
# for _ in range(II())
n,k,x = M()
a = L()
a.sort()
c=0
b=[]
for i in range(0,n-1):
    if (a[i+1]-a[i]>x): 
        l = (a[i+1]-a[i]-1)//x
        b.append(l)
b.sort()
while(len(b) != 0):
    k-=b[0]
    if (k>=0):
        b.pop(0)
    else:
        break
print(len(b)+1)