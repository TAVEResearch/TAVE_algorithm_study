# page: p571
# sol.1) brute force
from typing import List

def solution(nums: List[int], k: int) -> List[int]:
  answer = []
  for n in range(len(nums) - k + 1):
    answer.append(max(nums[n:n+k]))

  return answer

# result = [3, 3, 5, 5, 6, 7]
nums = [1, 3, -1, -3, 5, 3, 6, 7] # 6 = 8 - 3 + 1
k = 3

print(solution(nums, k))
