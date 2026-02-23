n = int(input())
contests = list(map(int, input().split()))
k=1
contests.sort()
i=0

while i < n:
    if contests[i] >= k:
        k += 1
    i+=1
print(k-1)
    


