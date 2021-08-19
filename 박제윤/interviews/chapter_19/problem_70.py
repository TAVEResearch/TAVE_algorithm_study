# page: p552
# sol) XOR
from typing import List

def singleNumber(nums: List[int]) -> int:
  result = 0

  for num in nums:
    result ^= num
  
  return result

# result = 1
nums = [2, 2, 1]

# result = 4
# nums = [4, 1, 2, 1, 2]

print(singleNumber(nums))
