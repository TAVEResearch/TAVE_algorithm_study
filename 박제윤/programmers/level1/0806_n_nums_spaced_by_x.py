# date: 2021.08.06
# author: jeiyoon
from typing import List

def solution(x: int, n: int) -> List[int]:
    return [ x + x * dist for dist in range(n)]
