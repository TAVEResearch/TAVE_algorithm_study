# date: 2021.08.17
# author: jeiyoon
from typing import List
import sys

# len(arr) >= 1: no empty list as an input 
# [Disclaimer!] you should not sort the array
def solution(arr: List[int]) -> List[int]:
  # exception
  if len(arr) == 1:
    return [-1]

  minimum = sys.maxsize

  for a in arr:
    if minimum > a:
      minimum = a 

  # arr.remove(min(arr))
  arr.remove(minimum)

  return arr
