
def func(array):

    if (len(array) == 0 or len(array) == 1):
        return len(array)

    max = array[0]
    min = abs(array[0]-array[1])
    # for i in array:
    #     if(max < i):
    #         max = i
    #     # if (min > i):
    #     #     min = i

    # a = True
    for i in range(len(array)):
        if (array[i]>max):
            max = array[i]
        j = i+1
        while(j<len(array)):
            if (abs(array[i]-array[j]) < min):
                min = abs(array[i]-array[j]) 
                # a = False
                # break
            j += 1

    if (max <= min):
        return len(array)

    if (len(array) == 2):
        return 1

    # newarr = []
    # for i in array:
    #     newarr.append(i)

    array.remove(max)
    # newarr.remove(max)

    # remMin = func(array)
    remMax = func(array)
    # if (remMin > remMax):
        # return remMin
    
    return remMax
    

    



num = int(input())

for i in range(num):

    n = int(input())
    array = input().split(" ")

    for j in range(n):
        array[j] = int(array[j])

    print(func(array))