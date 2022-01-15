a = ['a','e','i','o','u']

for _ in range(int(input())):
    s = input()
    n = len(s)

    k = -1
    c = 0
    for i in range(n):
        if (s[i] in a):
            c+= (n-i)*(i-k)
            k=i
    print(c)
