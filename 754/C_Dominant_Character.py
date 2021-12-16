for _ in range(int(input())):
    n  =int(input())
    s = input()
    a = -1
    pos = ['aa','aba','aca','abca','acba','abbacca','accabba']
    for i in pos:
        if i in s:
            a = len(i)
            break
    print(a)