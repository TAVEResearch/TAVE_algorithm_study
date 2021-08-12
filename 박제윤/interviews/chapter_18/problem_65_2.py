# page: p518
# sol.2) repeating

# Recursion -> repeating: simple!
from typing import List

def search(nums: List[int], target: int) -> int:
  left, right = 0, len(nums) - 1

  while left <= right:
    mid = (left + right) // 2

    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right mid - 1
    else:
      return mid
  
  return -1


nums = [-1, 0, 3, 5, 9 ,12] # sorted
target = 9

print(search(nums, target))
