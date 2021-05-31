def func(array):

    i = 0
    while (i < len(array)):
        if (i > 1):
            avg = int((array[i-2]+array[i])/2)
            if (avg == array[i-1]):
                temp = array[i]
                done = False
                j = i+1
                while (done == False and j<len(array)):
                    avg = int((array[i-2]+array[j])/2)
                    if (avg != array[i-1]):
                        done = True
                        array[i] = array[j]
                        array[j] = temp
                    j+=1

        # print(array)
        i+=1






num = int(input())

for i in range(num):

    n = int(input())
    array = input().split(" ")

    for j in range(2*n):
        array[j] = int(array[j])

    func(array)

    for j in range(2*n):
        print(array[j],end = " ")
    print("")
        