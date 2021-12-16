for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd,even = [],[]
    for i in a:
        if (i&1):odd.append(i)
        else:even.append(i)

    def maxx(ar):
        if(ar==[]):return 0
        return max(ar)

    bits = [len(bin ( i&(~(i-1)) )) -3 for i in even]
    even = [even[i]>>bits[i] for i in range(len(even))]
    print(sum(even) + sum(odd) + max(maxx(even), maxx(odd))*(pow(2, sum(bits))-1))