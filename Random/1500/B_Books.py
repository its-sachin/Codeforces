n,t = map(int,input().split())
a = list(map(int,input().split()))

i=j=0
for s in a:
    i+=s
    if(i>t):
        i-=a[j]
        j+=1
print(n-j)