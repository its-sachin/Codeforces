
def check(a,b):
    if(a[-1] == '0'):
        return False
    rev = a[::-1]
    for i in range(len(b)-len(a)+1):
        if(rev == b[i:i+len(a)] or a == b[i:i+len(a)]):
            j,k,valid = i,i+len(a),True
            while(j>=0):
                if(b[j] == '0'):
                    valid = False
                    break
                j-=1
            while(k<len(b)):
                if(b[k] == '0'):
                    valid = False
                    break
                k+=1
            if(valid):
                return True
        
    return False  

a,b = map(int,input().split())
a,b = bin(a)[2:],bin(b)[2:]
if(a==b or a+'1'==b or check(a,b) or check(a+'1',b) or check(a.strip('0'),b)):
    print('YES')
else:
    print('NO')