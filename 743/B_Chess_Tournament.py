for _ in range(int(input())):
    n=int(input())
    e=input()

    mat=[['X' for i in range(n)] for j in range(n)]

    for i in range(n):
        if(e[i]=='1'):
            for j in range(n):
                if(i!=j):
                    mat[j][i]='='
                    mat[i][j]='='

    done=False
    for i in range(n):
        if(e[i]=='2'):
            for j in range(n):
                if(i!=j and mat[i][j]=='X'):
                    mat[i][j]='+'
                    mat[j][i]='-'
                    break
            else:
                print("NO")
                done=True
                break

    if(not done):
        print("YES")
        for i in range(n):
            for j in range(n):
                if(i!=j and mat[i][j]=='X'):
                    mat[i][j]='='
                print(mat[i][j],end='')
            print('')
    