# def Convert(string):
#     list1=[]
#     list1[:0]=string
#     return list1

for _ in range(int(input())):
    s = input()
 
    n = len(s)
    count = 0
 
    i=0
    prev=0
    offset=0
    while(i<n):
        j=1
        f=-1
        if(s[i]!='?'):
            prev=int(s[i])
        else:
            f=0
        while(j+i<n):
            if(s[j+i]=='?'):
                if(f==-1):
                    f=j
                prev = 1-int(prev)
            else:
                if(prev==int(s[j+i])):
                    break
                prev=int(s[j+i])
                f=-1
            j+=1

        count+=(((j+offset)*(j+1+offset))//2)-((offset*(offset+1))//2)
        # print("part from",i,i+j,(((j+offset)*(j+1+offset))//2)-((offset*(offset+1))//2))
        if(s[i+j-1]=='?'):
            prev=1-prev
            offset=j-f
            # print("offset",offset)
        else:
            offset=0
        i+=j

    print(count)
 