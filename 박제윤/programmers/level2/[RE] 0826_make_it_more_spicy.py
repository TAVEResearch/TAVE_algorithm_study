# date: 2021.08.25
# author: jeiyoon
from typing import List

"""
It doens't work jesusπ’
"""


"""
# λͺ¨λ  μμμ μ€μ½λΉ μ§μκ° 7 μ΄μμ΄ λμκ³  μ΄λ μμ νμλ 2νμλλ€.
scovilleμ κΈΈμ΄λ 2 μ΄μ 1,000,000 μ΄νμλλ€.
Kλ 0 μ΄μ 1,000,000,000 μ΄νμλλ€.
scovilleμ μμλ κ°κ° 0 μ΄μ 1,000,000 μ΄νμλλ€.
"""
def solution(scoville: List[int], K: int) -> int:
    if len(scoville) <= 1:

    mixture_count = 0
    sorted_scoville = sorted(scoville, reverse=True)

    while len(sorted_scoville) >= 1:
        mixture_count += 1
        min_scoville = sorted_scoville.pop()
        second_min_scoville = sorted_scoville.pop()

        new_recipe = min_scoville + (2 * second_min_scoville)
        sorted_scoville.append(new_recipe)

        # exception: one component left and you can't reach to K
        if min(sorted_scoville) > K:
            answer = mixture_count
            break
        else:
            sorted_scoville = sorted(sorted_scoville, reverse=True)

    if sorted_scoville[0] < K:
        answer = -1

    return answer
# result = 2
# scoville = [1, 2, 3, 9, 10, 12]
# K = 7
scoville = []
print(scoville[0])
# K = 100
# print(solution(scoville, K))
