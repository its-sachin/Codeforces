def out(str):
    if (str[0] == "A"):
        start = "A"
        if (str[-1] == "A") :
            return "no"

        else:
            if (str[-1] == "B"):
                end = "B"
            else:
                end = "C"

    elif (str[0] == "B"):
        start = "B"
        if (str[-1] == "B"):
            return "no"

        else:
            if (str[-1] == "A"):
                end = "A"
            else:
                end = "C"

    else:
        start = "C"
        if (str[-1] == "C") :
            return "no"

        else:
            if (str[-1] == "B"):
                end = "B"
            else:
                end = "A"

    done = False
    mid = 0
    depth = 0
    for i in str:

        if (i == start) :
            depth += 1
        elif (i == end) :
            depth -= 1
            if (done and depth < 0):
                return "no"
        else :
            if (done) :
                depth += 1
            else:
                mid += 1
                if (depth < 0):
                    depth += mid
                    done = True
                    if (depth < 0):
                        return "no"

    if (done == False):
        if (depth > 0):
            depth -= mid
        else:
            depth += mid
    
    if (depth == 0) : return "yes"
    else: return "no"




n = int(input())


while(n>0):

    str = input()

    print(out(str))

    n -=1