# page: p504
# sol) Insertion sort
from typing import List

class Solution:
  # appropriate comparing function
  @staticmethod
  def to_swap(n1: int, n2: int) -> bool:
    return str(n1) + str(n2) < str(n2) + str(n1)

  # insertion sort
  def largestNumber(self, nums: List[int]) -> str:
    i = 1

    while i < len(nums):
      j = i

      while j > 0 and self.to_swap(nums[j - 1], nums[j]):
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j -= 1
      i += 1

    return str(int(''.join(map(str, nums))))

# result = "210"
input = [10, 2]

# result = "9534330"
# input = [3, 30, 34, 5, 9]

s = Solution()
print(s.largestNumber(input))

