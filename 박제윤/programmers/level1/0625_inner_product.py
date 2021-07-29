# date: 2021.06.25
# author: jeiyoon
from typing import List

def solution(a: List[int], b: List[int]) -> int:
    return sum([a_i * b_j for a_i, b_j in zip(a, b)])
