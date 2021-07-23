for _ in range(int(input())):
    n = input()
    m = 0
    for i in n:
        m = max(m,int(i))

    if(m==0):
        print(1)
    else:
        print(m)