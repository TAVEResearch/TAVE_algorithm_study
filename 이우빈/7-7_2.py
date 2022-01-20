from typing import List

# Using dictionary.
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]

        nums_map[num] = i


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))