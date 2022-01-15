

for _ in range(int(input())):
    n = int(input())
    array = input().split(" ")

    for i in range(n):
        array[i] = int(array[i])

    array.sort(reverse = True)
    # print(array)
    if (array[0] <0):
        if (n==1):
            print("YES") 
            print(n)
            print(array[0])
            continue
        else:
            print("NO")
            continue

    b = False
    for i in range(n):
        for j in range(i+1,n):
            if (array[i]==array[j] or (array[i] < 0 or array[j] < 0)):
                print("NO")
                b = True
                break
            else:
                done = False
                diff = array[i]-array[j]
                for k in range(i,n):
                    if (array[k] == diff): 
                        done = True
                        break
                if (done == False):
                    if (diff not in added):
                        added.append(diff)
                # print(added)
        if (b):
            break

    if(b == False):
        print("YES")
        print(n+len(added))
        for i in array:
            print(i,end = " ")
        for i in added:
            print(i,end = " ")


