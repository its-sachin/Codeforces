

def build(n):
    l=[1]*(n+1)
    t=4;upd=5
    while(t<=n):
        k=t
        while(k<=n):
            l[k]=t
            k+=t
        t+=upd
        upd+=2
    return l

psqr=build(100)
print(psqr)
# for _ in range(int(input())):
# 	n=int(input())
# 	a=list(map(int,input().split()))
# 	d={}
# 	mx=0
# 	for i in range(n):
# 		a[i]//=psqr[a[i]]
# 		t=d.get(a[i],0)+1
# 		d[a[i]]=t
# 		if(t>mx):
# 			mx=t
# 	print(mx)
