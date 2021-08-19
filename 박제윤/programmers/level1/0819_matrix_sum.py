# date: 2021.08.19
# author: jeiyoon
from typing import List

# Two matrices with equal rows and columns
def solution(arr1: List[List[int]], 
             arr2: List[List[int]]) -> List[List[int]]:
    
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
      result = [a1_i + a2_i for a1_i, a2_i in zip(a1,a2)]
      answer.append(result)
      
    return answer
