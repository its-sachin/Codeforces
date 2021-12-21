import random

file = open('input.txt','w+')

t = random.randint(1,3)
file.write(str(t)+'\n')
for i in range(t):
    file.write('\n')
    n = random.randint(1,10)
    m = random.randint(n,10)
    file.write(' '.join(map(str,[m,n])) + '\n')
    for i in range(m):
        p = []
        for j in range(n):
            p.append(random.randint(1,100))
        file.write(' '.join(map(str,p)) + '\n')

