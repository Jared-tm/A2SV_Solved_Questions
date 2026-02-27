n ,s = map(int,input().split())
arr = list(map(int, input().split()))

tot = 0
left = 0

window = float("inf")


for right in range(n):
    tot += arr[right]
    while tot - arr[left]>= s:
        tot -= arr[left]
        left += 1
    if tot >= s:   
        window = min(window, right - left +1)

if window == float("inf"):
    print(-1)
else:
    print(window)
