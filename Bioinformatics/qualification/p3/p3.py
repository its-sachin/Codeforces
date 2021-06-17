file = open("4.txt","r+") 
ans = open("ans.txt","w")

vertices = []
# parent,value,childs,height

n = int(file.readline())
for i in range(1,n+1):
    vertices.append((i,[]))

vertices[0][1].append(0)

a = map(int, file.readline())
for i in range(2,n+1):
    vertices[i-1][1].append(a[i-2])

a = map(int, file.readline())
for i in range(1,n+1):
    vertices[i-1][1].append(a[i-1])



