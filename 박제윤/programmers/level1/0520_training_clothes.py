# date: 2021.05.20
# author: jeiyoon

from typing import List

def solution(n: int, lost_n: List[int], reserve_n: List[int]) -> int:
    # reservers are in trouble
    reserve = [_ for _ in reserve_n if _ not in lost_n]
    lost = [_ for _ in lost_n if _ not in reserve_n]

    result = n - len(lost)

    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            result += 1
            reserve.remove(lost[i]-1)
        elif lost[i]+1 in reserve:
            result += 1
            reserve.remove(lost[i]+1)
        else:
            pass

    return result
