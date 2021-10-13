# date: 2021.08.25
# author: jeiyoon
from typing import List

"""
It doens't work jesus😢
"""


"""
# 모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
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
