from typing import List

def solution(n: int) -> List[int]:
    answer = []
    for _n in repr(n):
        answer.insert(0,int(_n))
    return answer

print(solution(12345))
