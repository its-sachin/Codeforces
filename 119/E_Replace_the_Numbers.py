class LL:
    def __init__(self, val) -> None:
        self.val = val
        self.last = self
        self.next = None
    def add(self, node):
        self.last.next = node
        self.last = node.last


d = {}; n =0
for _ in range(int(input())):
    k = list(map(int,input().split()))
    if(k[0] == 1):
        if(d.get(k[1])):
            d[k[1]].add(LL(n))
        else:
            d[k[1]] = LL(n)
        n+=1
    else:
        if(k[1] != k[2] and d.get(k[1])):
            if(d.get(k[2])):
                d[k[2]].add(d[k[1]])
            else:
                d[k[2]] = d[k[1]]
            d[k[1]] = None

a = [0]*n
for i in d:
    l = d[i]
    while(l):
        a[l.val] = i
        l = l.next
print(*a)
    
        

        