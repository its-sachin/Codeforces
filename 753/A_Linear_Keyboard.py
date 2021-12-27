for _ in range(int(input())):
    k = input()
    s = input()
    ans = 0
    for i in range(1,len(s)):
        ans += abs(k.index(s[i]) - k.index(s[i-1]))
    print(ans)