def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def func(array,n,m):

    i = 0
    firstO = False
    while(i < n):
        # print(m)
        # print("at i=" , i)
        # for a in range(n):
        #     print(array[a],end = "")
        # print("")

        if (array[i] == '1'):

            if (firstO == False):
                j = i-1
                while(j>=0 and j>= i-m):
                    array[j] = '1'
                    j-=1
                firstO = True
        
            
            j = i+1
            notF = True
            while(j<n and notF):
                if (array[j]=='1'):
                    notF = False
                else:
                    j+=1

            # print("i is ",i," j is ",j," notF is ", notF)
            if (notF):
                j = i+1
                # print(j,i+m,n)
                while(j<=i+m and j<n):
                    # print("kk")
                    array[j] = '1'
                    j+=1
                
                i = n
            else:
                a = i+1
                b = j-1
                while(a<b and a<=i+m and b>=j-m):
                    array[a] = '1'
                    array[b] = '1'
                    a+=1
                    b-=1
                
                i = j
                
        else:
            i+=1



    for i in range(n):
        print(array[i],end = "")
    print("")



num = int(input())

for i in range(num):
    n,m = input().split(" ")
    n,m = int(n),int(m)
    integer = (input())
    array = Convert(integer)
    # print(array)
    func(array,n,m)