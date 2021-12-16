f = open('a.txt', 'r')
test = []
soln = []

gotin = False
gotout = False
for line in f.readlines():
    if(line == 'Input\n'):
        gotin=True
    elif(line == 'Answer\n'):
        gotout=True
    elif(gotin):
        test.append(line[:-1])
        gotin=False
    elif(gotout):
        soln.append(line[:-1])
        gotout=False

f.close()

# print(len(soln))
for i in soln:
    print(i)
