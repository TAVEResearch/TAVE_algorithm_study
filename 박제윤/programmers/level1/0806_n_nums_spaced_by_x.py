from typing import List

def solution(x: int, n: int) -> List[int]:
    return [ x + x * dist for dist in range(n)]
