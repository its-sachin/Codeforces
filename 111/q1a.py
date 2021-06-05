for s in[*open(0)][1:]:
	S=i=0;P=[-1]*2;l=[-1]*2
	for c in s[:-1]:
		if'?'>c:p=int(c)^i&1;l[p]=i;P[p]=l[~p]
		S+=i-max(P);i+=1;
	print(S)

for _ in range(int(input())):

    s=input()
    S=i=0
    P=[-1]*2
    l=[-1]*2
    for c in s:
        if('?'>c):
            p