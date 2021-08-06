from typing import List

def solution(x: int, n: int) -> List[int]:
    answer = []
    increase = x

    for _ in range(n):
      answer.append(x)
      x = x + increase

    return answer
