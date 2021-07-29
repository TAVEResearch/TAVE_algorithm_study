# date: 2021.05.20
# author: jeiyoon
from typing import List

def solution(array: List[int], commands: List[List[int]]) -> List[int]:
    result = []
    # list.sort()
    # sorted(list)
    for c in commands:
        result.append(sorted(array[c[0]-1:c[1]])[c[2]-1])

    return result
