# page: p520
# sol.3) bisect module

# Note that it's quite better method: mid = left + (right - left) // 2
# to avoid overflow
from typing import List
import bisect

def search(nums: List[int], target: int) -> int:
  index  = bisect.bisect_left(nums, target)

  if index < len(nums) and nums[index] == target:
    return index
  else:
    return -1


nums = [-1, 0, 3, 5, 9 ,12] # sorted
target = 9

print(search(nums, target))
