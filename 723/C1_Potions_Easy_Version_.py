import heapq
n = int(input())
a = list(map(int,input().split()))
s =0; h = []
for i in a:
    s+=i
    heapq.heappush(h,i)
    if(s<0):
        s-= heapq.heappop(h)

print(len(h))