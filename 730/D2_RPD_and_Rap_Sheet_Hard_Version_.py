import sys

def xor(a,b,k):
    p=1
    ans=0
    while(a>0 or b>0):
        ans+=((a%k - b%k + k)%k)*p
        a//=k
        b//=k
        p*=k
    return ans

for _ in range(int(input())):
    n,k =map(int,input().split())
    done =0
    i=0
    while(done==0):
        if(i==0):
            print(0)
        else:
            if(i%2==0):
                print(xor(i,i-1,k))
            else:
                print(xor(i-1,i,k))
        done = int(input())
        sys.stdout.flush()
        i+=1
                    

    