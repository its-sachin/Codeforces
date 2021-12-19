for _ in range(int(input())):
    s = input()
    if(s.count('N') == 1 and s.count('E') > 0):
        print('NO')
    else:
        print('YES')