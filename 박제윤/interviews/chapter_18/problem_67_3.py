# page: p530
# sol.3) Two pointer
# O(NlogN): Sort -> "2Nlog(N)" for sorting + "2N" for comparing
from typing import List, Set
import bisect

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
  result: Set = set()

  nums1.sort()
  nums2.sort()
  i = j = 0

  # two pointer
  while i < len(nums1) and j < len(nums2):
    if nums1[i] > nums2[j]:
      j += 1
    elif nums1[i] < nums2[j]:
      i += 1
    else:
      result.add(nums1[i])
      i += 1
      j += 1

  return list(result)

# result = [2]
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

# result = [9, 4]
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4] 

print(intersection(nums1, nums2))
