n , limit = map(int,input().split())
arr = list(map(int, input().split()))
left = 0
tot = 0
res= 0
for right in range(n):
    tot += arr[right]
    while tot > limit:
        tot -= arr[left]
        left += 1
    res += right - left + 1
        
print(res)