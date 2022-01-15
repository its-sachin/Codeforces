def a2(s):
    n=len(s)
    if(n>1 and s[0]==s[1]):return s[0]*2
    i=1
    while(i<n):
        if(s[i]>s[i-1]):break
        i+=1
    c=s[:i]
    return c+c[::-1]

for _ in range(int(input())):
    n=int(input())
    s=input()
    print(a2(s))
    