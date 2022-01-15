def pf(n):
    c = 0
    while(n % 2 == 0):
        c+=1
        n = n // 2
    
    i=3
    while(i*i<=n):
         
        while (n % i== 0):
            c+=1
            n = n // i
        i+=2
             
    if n > 1:
        c+=1
    
    return c

for _ in range(int(input())):

    a,b,k = input().split(" ")
    a,b,k = int(a),int(b),int(k)

    if (k==0 and a==b):
        print("YES")

    elif (k==1):
        if ((a%b == 0 or b%a == 0)and a != b):
            print("YES")
        else:
            print("NO")
    
    else:
        p = pf(a) + pf(b)

        if (k>p):
            print("NO")

        else:
            print("YES")