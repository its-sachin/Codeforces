n=input()
done =True
for i in range(0,1000,8):
    start = -1
    done =True
    for j in str(i):
        start = n.find(j,start+1)
        if(start<0):
            done =False
            break
    if(done):
        print("YES\n",i)
        break
    done=False

if(not done):
    print("NO")


