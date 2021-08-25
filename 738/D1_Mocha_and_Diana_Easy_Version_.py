
from collections import defaultdict

class Graph:
  
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)
  

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
  
    def find_parent(self, parent,i):
        if parent[i] == -1:
            return i
        if parent[i]!= -1:
             return self.find_parent(parent,parent[i])
 
    def union(self,parent,x,y):
        parent[x] = y
 

    def isCyclic(self):
    
        parent = [-1]*(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent,x,y)
 

n,m1,m2=map(int,input().split())
g1=Graph(n)
g2=Graph(n)

for i in range(m1):
    u,v=map(int,input().split())
    g1.addEdge(u,v)

for i in range(m2):
    u,v=map(int,input().split())
    g2.addEdge(u,v)

ans=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i!=j and adj1[i].get(j)==None and adj2[i].get(j)==None):
            ans.append((i,j))
            adj1[i][j]=True
            adj1[j][i]=True
            adj2[i][j]=True
            adj2[j][i]=True

