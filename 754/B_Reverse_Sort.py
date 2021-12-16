for _ in range(int(input())):
    n = int(input())
    a = input()

    seq = []
    one = a.count('1')
    for i in range(n):
        if(a[i]=='1' and i<n-one):
            seq.append(i+1)
        elif(a[i]=='0' and i>=n-one):
            seq.append(i+1)
    
    if(len(seq)>0):
        print(1)
        print(len(seq),*seq)
    else:
        print(0)

    
