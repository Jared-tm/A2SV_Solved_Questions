
from collections import Counter
n , m = map(int, input().split()) 

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
res = 0
mapp1 = Counter(nums1)
mapp2 = Counter(nums2)

mapp1_key = set(mapp1.keys())
mapp2_key = set(mapp2.keys())

for num in mapp1_key:
    if num in mapp2_key:
        res += mapp1[num] * mapp2[num]

print(res)


