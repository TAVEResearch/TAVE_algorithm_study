# page: p518
# sol.1) recursion

# It should be noted that the limitation of recursion call is 1,000
# "Disclaimer": It's quite better method: mid = left + (right - left) // 2
# to avoid overflow
from typing import List

def search(nums: List[int], target: int) -> int:
  def binary_search(left: int, right: int) -> int:
    if left <= right:
#       mid = (left + right) // 2
      mid = left + (right - left) // 2    
  
      if nums[mid] < target:
        return binary_search(mid + 1, right)
      elif nums[mid] > target:
        return binary_search(left, mid - 1)  
      else: # nums[mid] == target
        return mid
    else: # error
      return -1

  return binary_search(0, len(nums) - 1) # left, right

nums = [-1, 0, 3, 5, 9 ,12] # sorted
target = 9

print(search(nums, target))
