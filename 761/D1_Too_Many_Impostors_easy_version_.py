for _ in range(int(input())):
    n = int(input())
    last = -1
    for i in range(n):
        print('?',i+1,(i+1)%n +1, (i+2)%n + 1)
        curr = int(input())
        if(last != -1 and curr != last):
            imp,crew = (i-1)%n + 1,(i+2)%n + 1
            if(last == 1): imp,crew = crew,imp
            break
        last = curr
    allimp = [imp]
    for i in range(1,n+1):
        if(i!= imp and  i!= crew):
            print('?',i,imp,crew)
            if(int(input()) == 0):
                allimp.append(i)
    print('!',len(allimp),*allimp)
        


        

                
