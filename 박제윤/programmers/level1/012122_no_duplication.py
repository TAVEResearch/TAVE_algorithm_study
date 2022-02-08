# date: 2022.01.21
# author: jeiyoon
from typing import List

def solution(arr: List[int]) -> List[int]:
  result = []

  for idx in range(len(arr) - 1):
    if arr[idx] != arr[idx + 1]:
      result.append(arr[idx])
  
  result.append(arr[-1]) # arr[-2] doesn't matter
  return result

# answer = 	[1,3,0,1]
# arr = [1,1,3,3,0,0,1]	

# anwer = [4,3]
arr = [4,4,4,3,3]

print(solution(arr))
