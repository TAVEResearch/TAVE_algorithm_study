# p571
# sol.1) brute force
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
  if not nums:
    return nums

  r = []

  for i in range(len(nums) - k + 1):
    r.append(max(nums[i:i+k]))

  return r

nums = [1, 3, -1, -3, 5, 3, 6, 7] # 6 = 8 - 3 + 1
k = 3
print(maxSlidingWindow(nums, k))
