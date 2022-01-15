for _ in range(int(input())):

    n = int(input())
    array = input().split(" ")

    sum = 0
    for i in array:
        sum += int(i)

    avg = sum/n

    # print("a",end = " ")
    if (avg != int(avg)):
        print(-1)
    else:
        avg = int(avg)
        gAvg = 0
        for i in array:
            if (int(i) > avg):
                gAvg += 1

        print(gAvg)
