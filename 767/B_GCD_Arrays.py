for _ in range(int(input())):
    l,r,k = map(int,input().split())
    o = (r-l+1)//2
    if(l%2==1 and (r-l)%2==0):o+=1

    if(k<o and not(o==1 and k==0 and l!=1 and l==r)):print("NO")
    else:print("YES")
