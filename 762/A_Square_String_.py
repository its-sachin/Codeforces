for _ in range(int(input())):
    s = input(); n =len(s)
    if(n&1): print('NO'); continue
    got = True
    for i in range(n//2):
        if(s[i]!=s[i+n//2]): got = False; break
    print('YES' if got else 'NO')