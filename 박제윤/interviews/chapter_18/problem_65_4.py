# page: p520
# sol.4) index()

# "Disclaimer": index() is not Binary search! 
from typing import List
import bisect

def search(nums: List[int], target: int) -> int:
  try:
    return nums.index(target)
  except ValueError: # target doesn't exist
    return -1


nums = [-1, 0, 3, 5, 9 ,12] # sorted
target = 9

print(search(nums, target))
