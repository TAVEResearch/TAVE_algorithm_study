# date: 2021.06.28
# author: jeiyoon
from typing import List

def solution(n: int, arr1: List[int], arr2:List[int]) -> List[str]:
    answer = []

    for a1, a2 in zip(arr1, arr2):
        # print("0" * (n - len(format(a1, 'b'))) + format(a1, 'b'))
        # print("0" * (n - len(format(a2, 'b'))) + format(a2, 'b'))
        a1_binary = format(a1, 'b').zfill(n)
        a2_binary = format(a2, 'b').zfill(n)

        wall = []

        for idx in range(n):
            if a1_binary[idx] == "1" or a2_binary[idx] == "1":
                wall.append("#")
            else:
                wall.append(" ")
        answer.append("".join(wall))

    return answer
