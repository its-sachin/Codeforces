# def f(a,l,k,i,ans):
#     if(i>=len(a)):
#         return ans
    
#     if(l==0):
#         return f(a,1,i,i+1,ans+1)+f(a,0,i,i+1,ans)
#     elif(l==1):
#         if(a[i]>a[k]):
#             return f(a,1,k,i+1,ans)+f(a,2,i,i+1,ans+1)
#         else:
#             return f(a,1,k,i+1,ans+1)
#     elif(l==2):
#         if(a[i]>a[k]):
#             return f(a,2,k,i+1,ans)
#         else:
#             return f(a,2,k,i+1,ans+1)

def f(a,l,k,l2,k2,i,ans):
    if(i>=len(a)):
        print(l,k,l2,k2,ans)
        return ans
    
    if(l==0):
        return f(a,1,i,1,i,i+1,ans+1)+f(a,0,i,0,i,i+1,ans)
    elif(l==1):
        if(a[i]>a[k]):
            return f(a,1,k,l2,k2,i+1,ans)+f(a,2,i,l2,k2,i+1,ans+1)
        else:
            if(l2==1):
                if(a[i]<a[k2]):
                    return f(a,1,k,1,k2,i+1,ans)+f(a,1,k,2,i,i+1,ans+1)
                else:
                    return f(a,1,k,1,k2,i+1,ans+1)
            elif(l2==2):
                if(a[i]<a[k2]):
                    return f(a,1,k,2,k2,i+1,ans)
                else:
                    return f(a,1,k,2,k2,i+1,ans+1)

    elif(l==2):
        if(a[i]>a[k]):
            return f(a,2,k,l2,k2,i+1,ans)
        else:
            if(l2==1):
                if(a[i]<a[k2]):
                    return f(a,2,k,1,k2,i+1,ans)+f(a,2,k,2,i,i+1,ans+1)
                else:
                    return f(a,2,k,1,k2,i+1,ans+1)
            elif(l2==2):
                if(a[i]<a[k2]):
                    return f(a,2,k,2,k2,i+1,ans)
                else:
                    return f(a,2,k,2,k2,i+1,ans+1)



for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(f(a,0,-1,0,-1,0,0)-1)
    
