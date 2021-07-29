# date: 2021.06.29
# author: jeiyoon
from typing import List

def solution(d: List[int], budget: int) -> int:
    answer = []
    list_sum: int = 0
    for dep in sorted(d):
        list_sum += dep
        if list_sum <= budget:
            answer.append(dep)
        else:
            break

    return len(answer)
