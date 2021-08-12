# page: p530
# sol.2) Binary Search
# O(NlogN)
from typing import List, Set
import bisect

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
  result: Set = set()

  nums2.sort()

  for n1 in nums1:
    # binary search
    i2 = bisect.bisect_left(nums2, n1)

    if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
      result.add(n1)

  return list(result)

# result = [2]
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

# result = [9, 4]
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4] 

print(intersection(nums1, nums2))
