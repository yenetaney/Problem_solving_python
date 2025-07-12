def two_sum(nums, target):
    seen = {}
    for i , num in enumerate(nums):
        x = target - num
        if x in seen:
            return [seen[x],i]
        seen [num] = i

result = two_sum([2, 7, 11, 15], 9)
print(result)