n , k = map(int,input().split())
nums = list(map(int , input().split()))
gaps = []
for i in range(1, n):
    gaps.append(nums[i]-nums[i-1])

cost = nums[-1] - nums[0]

gaps.sort(reverse=True)
for i in range(k-1):
    cost -= gaps[i]
print(cost)