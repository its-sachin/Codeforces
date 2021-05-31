def func(array):
    min = -1
    for i in array:
        if(min == -1 or min >i):
            min = i
    count =0
    for i in array:
        if (i > min):
            count += 1

    return count




num = int(input())

for i in range(num):

    n = int(input())
    array = input().split(" ")

    for j in range(n):
        array[j] = int(array[j])

    print(func(array))