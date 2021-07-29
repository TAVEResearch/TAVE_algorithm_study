# date: 2021.05.21
# author: jeiyoon

from typing import List
from collections import defaultdict

def solution(N: int, stages: List[int]) -> List[int]:
    answer = []
    failure_dict = defaultdict(float)
    norm_constant = len(stages)

    for stg in range(1, N + 1): # stage 1 to N
        try:
            failure_dict[stg] = stages.count(stg) / norm_constant
        except: # denominator is zero
            failure_dict[stg] = 0
        norm_constant -= stages.count(stg)

    for k, _ in sorted(failure_dict.items(),
                         key = lambda x: x[1],
                         reverse = True):
        answer.append(k)

    return answer
