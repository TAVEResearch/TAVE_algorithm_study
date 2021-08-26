# p572
# sol.2) optimization using queue
from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
  results = []
  window = deque()
  current_max = float('-inf')

  for i,v in enumerate(nums):
    window.append(v)

    if i < k - 1:
      continue
    
    # change if the new one is bigger than the previous one
    if current_max == float('-inf'):
      current_max = max(window)
    elif v > current_max:
      current_max = v

    results.append(current_max)

    # reset if the max value pops
    if current_max == window.popleft():
      current_max = float('-inf')

  return results

nums = [1, 3, -1, -3, 5, 3, 6, 7] # 6 = 8 - 3 + 1
k = 3
print(maxSlidingWindow(nums, k))
