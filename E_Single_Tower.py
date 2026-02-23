n = int(input())
towers = []
all_towers = []

splt = 0

for _ in range(n):
    arr = list(map(int, input().split() ))
    towers.append(arr[1:])
    all_towers.extend(arr[1:])

all_towers.sort()

order_map = {}
for i in range (len(all_towers)-1):
    order_map[all_towers[i]] = all_towers[i+1]

for tower in towers:
    for i in range(len(tower)-1):
        if order_map.get(tower[i]) != tower[i+1]:
            splt +=1
comb = n+splt-1

print(splt,comb)
