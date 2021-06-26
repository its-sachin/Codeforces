def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())
# for _ in range(II())

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

n,q = M()
s = I()
a = [0]*n
a[0] = d.get(s[0])
for i in range(1,n):
    a[i] = a[i-1] + d.get(s[i])

for _ in range(q):
    l,r = M()
    if (l<2):
        c = a[r-1]
    else:
        c=a[r-1]-a[l-2]

    print(c)