n , k = map(int,input().split())
arr = list(map(int, input().split()))
 
seen = {}
left = 0
 
ans= 0
 
for right in range(len(arr)):
    seen[arr[right]] = seen.get( arr[right] , 0) +1 
    while len(seen) > k:
        seen[arr[left]] -= 1
        if seen[arr[left]] == 0:
            del seen[arr[left]] 
        left += 1
    ans += (right-left + 1)
       
print(ans)