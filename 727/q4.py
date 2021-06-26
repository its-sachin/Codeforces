def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())
# for _ in range(II())
n = II()
a = []
b = []
for i in range(n):
    ai,bi = M()
    a.append(ai)
    b.append([bi,i])
b.sort(reverse=True)
# print(b)
s=0
c=0
for i in range(n):

    if (c>=b[i][0]):
        s+=a[b[i][1]]
    else:
        if (c+a[b[i][1]]>b[i][0]):
            if (a[b[i][1]]<b[i][0]-c):
                s+=a[b[i][1]]*2
            else:
                s+=a[b[i][1]]-c+b[i][0]
        else:
            s+=a[b[i][1]]*2
    c+=a[b[i][1]]
print(s-1)
        