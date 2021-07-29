# date: 2021.05.17
# author: jeiyoon
from typing import List

def solution(nums: List[int]) -> int:
    d_nums : List[int] = list(set(nums)) # Deduplication

    if len(d_nums) <= len(nums) / 2:
        answer = len(d_nums)
    else:
        answer = len(nums) / 2

    return int(answer)
