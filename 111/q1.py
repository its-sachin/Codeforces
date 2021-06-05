

for _ in range(int(input())):
    si= input().split(" ")
    
    m1 = 0
    m2 = 0

    for i in si:
        if (int(i) > m1):
            m2 = m1
            m1 = int(i)
        elif(int(i) > m2):
            m2 = int(i)

    w1 = max(int(si[0]), int(si[1]))
    w2 = max(int(si[2]), int(si[3]))

    if((w1 == m1 and w2 == m2) or (w2 == m1 and w1 == m2) ):
        print("YES")
    else:
        print("NO") 


    
