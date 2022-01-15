import random
import subprocess

file = open("in.txt","w") 

t = random.randint(1,2)
file.write(str(t)+"\n")

for _ in range(t):
    n = random.randint(3,10)
    file.write(str(n)+"\n")
    d = []
    i=0
    while(i<n-1):
        a = random.randint(1,n)
        b = random.randint(1,n)
        if (a!=b):
            w = random.randint(1,100)
            file.write(str(a) + " " + str(b) + " " + str(w) + "\n")
            i+=1

file.close()

# subprocess.run("python q7.py ", shell = True)
# subprocess.run("python q7Naive.py ", shell = True)

# f1 = open("a1.txt","r+").readlines()
# f2 = open("a2.txt","r+").readlines()

# if (len(f1) != len(f2)):
#     print("Length unequal ", len(f1), len(f2))
# else:
#     for i in range(len(f1)):
#         if (f1[i] != f2[i]):
#             print("Unequal at line ",i,f1[i],f2[i])