# page: p525
# sol) Binary Search

# No Numpy!
from typing import List

def search(nums: List[int], target: int) -> int:
  left, right = 0, len(nums) - 1
  while left < right:
    mid = left + (right - left) // 2
    
    if nums[mid] > nums[right]:
      left = mid + 1
    else:
      right = mid

  return mid # pivot

# result = 5
nums = [4, 5, 6, 7, 0, 1, 2] # partially sorted
target = 1

print(search(nums, target))
