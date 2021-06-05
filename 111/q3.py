def Convert(string):
    list1=[]
    list1[:0]=string
    return list1


for _ in range(int(input())):
    s = Convert(input())

    n = len(s)
    count = 0

    i = 0
    while (i<n):
        # print("i ",i)
        start = i
        qcount = 0
        found = False
        temp = 0
        j=i
        last = False
        enc = False
        while(j<n):
            # print("j is " ,j)
            if (i == j):
                if (s[i] == '?'):
                    qcount += 1
                    last = True
                else:
                    enc = True
                    temp += 1
                
                j+=1
            else:
                if (s[j] != '?'):
                    enc = True
                    if (s[j] == s[j-1]):
                        break

                    else:
                        if (found == False):
                            temp += 1
                            j+=1
                        else:
                            # print("i is ",i," qcount is ",qcount," start is ",start," s[j] is ",s[j]," count is ",count)
                            found = False

                            if (s[start] == s[j]):
                                if (qcount%2 == 1):
                                    temp += qcount+1
                                    j+=1
                                else:
                                    j = start+1
                                    break
                            else:
                                if (qcount%2 == 0):
                                    temp += qcount+1
                                    j+=1
                                else:
                                    j = start+1
                                    # print("break")
                                    break
                            
                            qcount = 0
                         

                else:

                    if (found == False and enc == True):
                        found = True
                        start = j-1
                    qcount += 1
                    j+=1
                    last = True
        
        if (last):
            temp += qcount
        print(temp)
        count += int(((temp+1)*temp)/2)
        i = j
        

    
  
    print(count)



            
