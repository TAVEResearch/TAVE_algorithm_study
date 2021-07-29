# date: 2021.06.30
# author: jeiyoon
from typing import List
from collections import defaultdict

def solution(lottos: List[int], win_nums: List[int]) -> List[int]:
    answer = []
    rank_dict = defaultdict(int)
    num_of_last_place: int = 6 # last place: 6th
    top_rank, lowest_rank = 0, 0

    # create a ladder
    for value, key in enumerate(reversed(range(num_of_last_place))):
        rank_dict[key + 1] = value + 1

    rank_dict[0] = num_of_last_place

    # calculate the top and lowest rank
    for l in lottos:
        if l == 0:
            top_rank += 1
        elif l in win_nums:
            top_rank += 1
            lowest_rank += 1
        else:
            pass
        
    answer.append(rank_dict[top_rank])
    answer.append(rank_dict[lowest_rank])
    
    return answer
