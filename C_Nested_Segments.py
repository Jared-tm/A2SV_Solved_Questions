n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r, i + 1))
segments.sort(key=lambda x: (x[0], -x[1]))

max_r = 0
max_r_idx = -1
found = False

for l, r, idx in segments:
    if r <= max_r:
        print(f"{idx} {max_r_idx}")
        found = True
        break 
    else:
        max_r = r
        max_r_idx = idx
if not found:
    print(-1, -1)