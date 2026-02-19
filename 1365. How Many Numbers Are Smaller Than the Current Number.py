nums = [8,1,2,2,3]
res =[]
pos  = {}
sorted_nums = sorted(nums)
unique = set()
for i in range(len(sorted_nums)):
    if (sorted_nums[i]) not in unique:
        unique.add(sorted_nums[i])
        pos[sorted_nums[i]] = i
for num in nums:
    res.append(pos[num])
print (res)

            