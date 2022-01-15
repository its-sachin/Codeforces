import sys;import math;from collections import deque;from bisect import bisect_left,bisect_right;I=sys.stdin.readline;II=lambda :int(I());IN=lambda x:map(int,x.split());FN=lambda x:map(float,x.split());L=lambda x:list(IN(x));M=1000000007;P=print;T=True;F=False
y=[0];i=[0];t=[0];m=1;f=F
def update(l,n,k):
	i=0
	while(i<n):
		l[i]+=1
		if(l[i]<k):
			return l,n
		l[i]=0
		i+=1
	l.append(1)
	y.append(0)
	t.append(0)
	return l,n+1
def xor(a,b,k,f=False):
	i=0;l=[]
	if(f):
		while(i<m):
			l.append((a[i]+b[i]) % k)
			i+=1
	else:
		while(i<m):
			l.append((a[i]-b[i]) % k)
			i+=1
	return l
def disp(t,k):
	j=1;s=0
	for i in t:
		s+=j*i
		j*=k
	return s
for _ in range(II()):
	n,k=IN(I());r=0
	y=[0];i=[0];t=[0];m=1;f=F
	while(r==0):
		P(disp(t,k))
		i,m=update(i,m,k)
		t=xor(y,i,k,f)
		f^=True
		y=xor(t,y,k)
		sys.stdout.flush()
		r=II()
	if(r==-1):
		P('wrong h')