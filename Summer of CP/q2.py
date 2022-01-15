# fast IO
import sys
input = sys.stdin.readline
def print(x, end='\n'):
    sys.stdout.write(str(x) + end)

# IO helpers
def get_int():
    return int(input())
def get_list_ints():
    return list(map(int, input().split()))
def get_char_list():
    s = input()
    return list(s[:len(s) - 1])
def get_tuple_ints():
    return tuple(map(int, input().split()))
def print_iterable(p):
    print(" ".join(map(str, p)))

def main():

    
    for _ in range(int(input())):

        n = get_int()
        a = get_list_ints()
        b = [0]*n

        # //0=unchecked
        # 1 = acha
        # -1 = kharab

        i=0
        c=0
        while(i<n):
            if (b[i] == 0):
                j = i+a[i]
                l = [i]
                while(True):
                    if ((j>=n or j<0) or b[j] == 1):
                        for k in l:
                            b[k] = 1
                            c+=1
                        break
                    elif (b[j]==-1):
                        break
                    l.append(j)
                    b[j]=-1
                    j=j+a[j]
            i+=1

        print(c)
                
        for i in range(n):
            if (b[i]==1):
                print(i+1,end=" ")
        print("")

    pass

if __name__ == '__main__':
    main()