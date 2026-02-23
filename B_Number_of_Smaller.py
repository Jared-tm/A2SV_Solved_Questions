n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
res = []
for num in b:
    while i<n and a[i] < num:
        i += 1
    res.append(i)
print(*res)

