from bisect import bisect_left, bisect_right
import math

for _ in range(int(input())):
    n,k,x = map(int,input().split())
    s = input()

    if(x == 1 or s.count('*') == 0):print('a'*(s.count('a'))); continue

    a = [1]; pos = []
    last = n-1
    while(last >=0 and s[last] == 'a'): last -=1
    c = 0
    while(last >=0 and s[last]== '*' ) : 
        last -=1; c+=1
    a.append(c*k +1)
    if(c!=0): pos.append([last+1,c*k])

    while(last>=0):
        while(last >=0 and s[last] == 'a'): last -=1
        c = 0
        if(last <0): break
        while(last >=0 and s[last]== '*' ) : 
            c += 1
            last -=1
        a.append(a[-1]*(k*c + 1))
        pos.append([last+1,k*c])

    ind = bisect_left(a,x)
    p = a[ind-1]
    
    d = math.ceil(x/p)
    left = d*p - x
    pos[ind-1][1] = d-1

    # print(left)
    for i in range(ind-2,-1,-1):
        if(left >= a[i+1]-a[i]):
            pos[i][1] = 0
            left -= a[i+1] - a[i]
        else:
            j = left//a[i]
            if(j == 0 and i == 0):
                pos[i][1] -= left
                left = 0
            else:
                left %= a[i]
                pos[i][1] -= j
            
        if(left== 0):break

    # print(a,ind,left,pos)
    i = 0; ans = ''; last = len(pos)
    while(i<n):
        while(i<n and s[i] == 'a'):
            ans += 'a'; i+=1
        if(i>=n): break
        while(i<n and s[i] == '*'):
            i += 1
        last -= 1

        if(last < ind):
            ans += 'b'*(pos[last][1])
    print(ans)