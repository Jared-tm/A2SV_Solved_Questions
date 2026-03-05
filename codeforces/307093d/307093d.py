n , s = map(int,input().split())
arr = list(map(int, input().split()))

left = 0
tot = 0
ans= 0

for right in range(len(arr)):
    tot += arr[right]
    while tot >= s:
        ans += (n -right )
        tot -= arr[left]
        left += 1
print(ans)