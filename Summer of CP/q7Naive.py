file = open("in.txt","r+") 
ans = open("a2.txt","w") 

for _ in range(int(file.readline())):
    n = int(file.readline())
    a = [int(x) for x in file.readline().split()]

# for _ in range(int(input())):
#     n = int(input())
#     a = [int(x) for x in input().split()]
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if ((a[i]**4 - a[j]**4)%8==0):
                # print(a[i],a[j])
                c+=1

    # print("\n")
    # print(c)
    ans.write(str(c)+"\n")