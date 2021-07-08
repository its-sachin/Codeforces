a = input()
ab = [-1,-1]
ba = [-1,-1]

for i in range(len(a)-1):
    if(a[i:i+2] == "AB"):
        if(ab[0]==-1):
            ab[0]=i
        else:
            ab[1]=i
    elif(a[i:i+2]=="BA"):
        if(ba[0]==-1):
            ba[0]=i
        else:
            ba[1]=i

if((ba[0]==-1 or ab[0]==-1) or (ba[1]==-1 and ab[1]==-1 and (ba[0] == ab[0]+1 or ab[0]==ba[0]+1)) or (ba[1]==-1 and ba[0] == ab[1]-1 and ba[0] == ab[0]+1) or (ab[1]==-1 and ab[0]==ba[1]-1 and ab[0]==ba[0]+1)):
    print("NO")
else:
    print("YES")