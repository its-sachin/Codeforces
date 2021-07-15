for _ in range(int(input())):
    n,a,b = map(int,input().split())
    s = input()    

    if(b<0):
        one=0
        zero=0
        if(s[0]=='1'):
            one+=1
        else:
            zero+=1

        for i in range(n-1):
            if(s[i]=='0' and s[i+1]=='1'):
                one+=1 
            if(s[i]=='1' and s[i+1]=='0'):
                zero+=1

                        
        print(a*n+b*(min(one,zero)+1))

        


    else:
        print((a+b)*n)

