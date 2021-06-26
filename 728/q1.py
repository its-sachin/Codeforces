def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
for _ in range(II()):
    n = II()
    if(n%2==0):
        i=1
        while(i<n):
            print(i+1,i,end = " ")
            i+=2
    else:
        i=1
        while(i<n-3):
            print(i+1,i,end=" ")
            i+=2
        print(n,n-2,n-1)