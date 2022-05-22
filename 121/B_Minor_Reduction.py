for _ in range(int(input())):
    n = [ord(c) - ord('0') for c in input()]
    got = False
    for i in range(len(n)-1,0,-1):
        if(n[i]+n[i-1]>9):
            v=n[i]+n[i-1]
            n[i-1]=v//10
            n[i]=v%10
            got = True
            break
    if(not got):
        n[1]+=n[0]
        n=n[1:]
    print(''.join(map(str,n)))
        