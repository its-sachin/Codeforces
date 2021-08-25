d=[]
k=1
while(len(d)<1000):
    if(k%3!=0 and str(k)[-1]!='3'):
        d.append(k)
    k+=1
# print(d)
for _ in range(int(input())):
    k=int(input())
    print(d[k-1])