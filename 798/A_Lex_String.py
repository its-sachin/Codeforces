for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=sorted(input())
    b=sorted(input())
    i=0;j=0
    d=[a,b]
    c='';f=0;l=-1
    while i<n and j<m:
        if(a[i]<b[j]):
            if(f==k):
                if(l==0):c+=b[j];j+=1;l=1;f=1
                else:c+=a[i];f+=1;i+=1;l=0;f=1
            else:
                c+=a[i];i+=1
                if(l==0):f+=1
                else:f=1;l=0

        else:
            if(f==k):
                if(l==1):c+=a[i];i+=1;l=0;f=1
                else:c+=b[j];f+=1;j+=1;l=1;f=1
            else:
                c+=b[j];j+=1
                if(l==1):f+=1
                else:f=1;l=1
    print(c)
