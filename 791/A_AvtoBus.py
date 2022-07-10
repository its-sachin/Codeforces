for _ in range(int(input())):
    n=int(input())
    if(n&1 or n==2):print(-1);continue
    k=n//2
    m1=k//3 if k%3==0 else k//3+1
    print(m1,k//2)
