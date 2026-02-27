n ,s = map(int,input().split())
arr = list(map(int, input().split()))


tot = 0
left = 0

window = 0

for right in range(n):
    tot += arr[right]
    while tot > s:
        tot -= arr[left]
        left += 1
    
    window = max(window, right - left +1)

if window == 0:
    print(0)
else:
    print(window)

    



