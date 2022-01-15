import random
file = open('in.txt','w+')

t = random.randint(10,40)
file.write(f'{t}\n')

for _ in range(t):
    n,m=10,10
    file.write(f'\n{n} {m}\n')
    for i in range(n+1):
        s=''
        for j in range(m):
            s += str(random.randint(0,9))
        file.write(s+'\n')