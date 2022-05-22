for _ in range(int(input())):
    s=list(map(int,list(input())))
    print('YNEOS'[sum(s[:3])!=sum(s[3:])::2])