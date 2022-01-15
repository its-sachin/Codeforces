import subprocess
import time

while True:
    subprocess.run('python inp.py')

    print('running e1')
    st=time.time()
    subprocess.run('python e1.py <in.txt >out.txt',shell=True)
    print(time.time()-st)

    print('running e2')
    st = time.time()
    subprocess.run('python E_Masha_forgetful.py <in.txt >outmy.txt',shell=True)
    print(time.time()-st)

    f1=open('out.txt','r+').readlines()
    f2=open('outmy.txt','r+').readlines()
    print(f1,f2)
    if(f1!=f2):break