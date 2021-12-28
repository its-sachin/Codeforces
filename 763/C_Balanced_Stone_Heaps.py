import random, math

def a2(n,a,i):
    if(i==n):return min(a),a
    k = a[i]//3
    ans = [0,-1]
    for d in range(0,k+1):
        c = []
        c[:] = a[:]
        c[i] -= 3*d
        c[i-1] += d
        c[i-2] += 2*d
        aa = a2(n,c,i+1)
        if(aa[0]>ans[0]):
            ans = aa
    return ans

def a1(n,a):
    mn = min(a)
    for i in range(2,n):
        a1,a2=0,0
        if(i+1<n):a1=a[i+1]//3
        if(i+2<n):a2=a[i+2]//3
        x = math.ceil(a[i]+a1+a2-mn)//3
        prev = a[i]
        a[i] -= 3*x
        a[i-1] += x
        a[i-2] += 2*x

        if(mn==prev):mn=max(mn,a[i])
        mn = min(a[i],mn)
    return min(a),a

# for _ in range(int(input())):
#     n=int(input())
#     a=list(map(int,input().split()))
#     print(a2(n,a,2))



while True:
    n = random.randint(3,4)
    a = []
    for i in range(n):
        a.append(random.randint(1,10))
    c = []
    c[:] = a[:]
    print(a)
    an1,ab1 = a1(n,a)
    an2,ab2 = a2(n,c,2)

    if(an1!=an2):print(an1,an2);print(ab1,ab2);break