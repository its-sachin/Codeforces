for _ in range(int(input())):
    n = input()
    s = [1 - int(x)%2 for x in n]
    print(0) if s[-1] else print(1) if s[0] else print(2) if sum(s) else print(-1)