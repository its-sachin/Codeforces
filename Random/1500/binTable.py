import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
for _ in range(II()):
    n,m=M()
    a = []
    for i in range(n):
        a.append(I())
    k=0
    s = [0,3,2,1,4]
    
    def ans(a,i,j,n,m,step):

        one = []
        zero = []

        def val(i,j):
            ans = int(a[i][j])
            if(ans==1):
                one.append((i,j))
            else:
                zero.append((i,j))
            return ans

        c = val(i,j)
        if(i!=n-1):
            c+=val(i+1,j)
            if(j!=m-1):
                c+=val(i+1,j+1)+val(i,j+1)
            else:
                zero.append((i,j-1))
                zero.append((i+1,j-1))
        else:
            zero.append((i-1,j))
            if(j!=m-1):
                c+=val(i,j+1)
                zero.append((i-1,j+1))
            else:
                zero.append((i-1,j-1))
                zero.append((i,j-1))

        def steps():
            # print(zero,one)
            if (len(one)==0):
                return
            elif(len(one)==3):
                for i in one:
                    step.append(i)
            elif(len(one)==2 or len(one)==1):
                for i in range(2):
                    step.append(zero[0])
                    one.append(zero.pop(0))
                step.append(one[0])
                zero.append(one.pop(0))
                steps()
            else:
                for i in range(3):
                    step.append(one[0])
                    zero.append(one.pop(0))
                steps()

        steps()
        return c
                
    step=[]
    for i in range(0,n,2):
        for j in range(0,m,2):
            c = ans(a,i,j,n,m,step)
            k+=s[c]

    print(k)
    for i in range(0,len(step),3):
        for k in range(3):
            print(step[i+k][0]+1,step[i+k][1]+1,end=" ")
        print("")