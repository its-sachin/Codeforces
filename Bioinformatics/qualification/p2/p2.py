def part(M, left, right):

    out = left-1
    pivot = M[right]
    
    i = left
    while(i < right):
        if (M[i][0] < pivot[0] ):
            out+= 1

            temp = M[out]
            M[out] = M[i]
            M[i] = temp
        i +=1
    
    out += 1
    temp = M[right]
    M[right] = M[out]
    M[out] = temp

    return out

def sortC(M, low, high):

    while(low<high):
        
        pivot = part(M,low,high)

        sortC(M,low,pivot-1)
        sortC(M,pivot+1,high)

def search(a, n, val):
 
    if (val <= a[0][0]):
        return 0
    if (val >= a[n - 1][0]):
        return n - 1

    i = 0
    j = n 
    mid = 0
    while (i < j):
        mid = (i + j) // 2
 
        if (a[mid][0] == val):
            return mid
 
        if (val < a[mid][0]) :

            if (mid > 0 and val > a[mid - 1][0]):

                if (val - a[mid - 1][0] >= a[mid][0] - val):
                    return mid
                else:
                    return mid - 1
 
            j = mid
         
        else :

            if (mid < n - 1 and val < a[mid + 1][0]):

                if (val - a[mid][0] >= a[mid+1][0] - val):
                    return mid+1
                else:
                    return mid
                 
            i = mid + 1
         
    return mid

def readArr(a,s,n):
    i=0
    w=""
    for x in s:
        if (x==' '):
            a.append([float(w),i+1])
            w=""
            i+=1
        else:
            w+=x

    if (i<n):
        a.append([float(w),i+1])

file = open("4.txt","r+") 
ans = open("ans.txt","w") 

t = int(file.readline())

for q in range(t):

    print("testcase progress",(q/t)*100)

    m,k,n = map(int,file.readline().split())

    s = file.readline()
    meta=[]
    readArr(meta,s,m)

    s = file.readline()
    adduct=[]
    readArr(adduct,s,k)

    s = file.readline()
    signal=[]
    readArr(signal,s,n)

    meta.sort()


    
    for j in range(n):

        print("progress", (j/n)*100,end="\r")

        val = signal[j][0]
        done = False
        minS = float('inf')
        for ki in range(k):

            kv = adduct[ki][0]
            searched = search(meta,m,val-kv)

            if (searched != -1):
                # print("at index",adduct[ki][1],"finding",val-kv,"found",meta[searched][0],"index",meta[searched][1] )

                if (meta[searched][0]== val-kv):
                    ans.write(str(meta[searched][1]) + " " + str(adduct[ki][1]) + "\n")
                    done =True
                    break

                if ((kv+meta[searched][0])>0 and minS>abs(val-kv-meta[searched][0])):
                    minIn = [searched,ki]
                    minS = abs(val-kv-meta[searched][0])

            # else:
            #     print("at",kv,"finding",val-kv,"not found")
        if (done==False):
            ans.write(str(meta[minIn[0]][1]) + " " + str(adduct[minIn[1]][1]) + "\n")

