n = 1000000
nums = [True] * n
for i in range(2, int(n**0.5) + 1):
    if nums[i]:
        for j in range(i*i, n, i):
            nums[j] = False
allprimes = {}
for i in range(2, n):
    if nums[i]:
        allprimes[i] = True

for _ in range(int(input())):
    n,e = map(int,input().split())
    a = list(map(int,input().split()))

    ones = [0]*n
    primes = [-1]*n
    for i in range(n-1,-1,-1):
        if a[i] == 1:
            if(i+e >= n):
                ones[i] = 1
            else:
                ones[i] = ones[i+e] + 1
                primes[i] = primes[i+e]

        if allprimes.get(a[i]):
            if(i+e >= n):
                primes[i] = i
            else:
                primes[i] = i

    count = 0
    for i in range(n-e):
        if(allprimes.get(a[i])):
            count += ones[i+e]
        elif(ones[i] >0 and primes[i] != -1):
            count += 1
            if(primes[i] + e < n):
                count += ones[primes[i] + e]
    print(count)


