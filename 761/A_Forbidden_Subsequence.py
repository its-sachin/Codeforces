for _ in range(int(input())):
    s = input()
    t = input()
    a,b,c = 'a'*s.count('a'),'b'*s.count('b'),'c'*s.count('c')
    k,done = [],['a','b','c']
    for i in s:
        if(i not in done):
            k.append(i)
    k.sort()
    ans = ''
    if(t=='abc' and a!=''):
        ans = a+c+b
    else:
        ans = a+b+c

    for i in k:
        ans += i

    print(ans)