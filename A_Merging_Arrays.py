n, m= map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

p1 = 0
p2 = 0
res=[]


while p1 < n and p2 <m:
    if nums1[p1] <= nums2[p2]:
        res.append(nums1[p1])
        p1 += 1
    else:
        res.append(nums2[p2])
        p2 += 1
if p1 < n:
    res.extend(nums1[p1+1])
elif p2 < m:
    res.extend(nums2[p2:])

print(*res)