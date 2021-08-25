# date: 2021.08.25
# author: jeiyoon
from typing import List
import math

def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    answer, days = [], []

    # calculate the days left
    for p, s in zip(progresses, speeds):
        day_left = math.ceil((100 - p) / s)
        days.append(day_left)

    # calculate the progress
    for idx in range(len(days)):
        # init
        if idx == 0:
            min_day = days[0]
            continue
        if days[idx] <= min_day:
            days[idx] = min_day
        else: # days[idx] > min_day
            min_day = days[idx]

    overlap = 1

    # check the duplications
    for idx in range(len(days) - 1):
        if days[idx] == days[idx + 1]: # same
            overlap += 1
            if idx == len(days) - 2: # last comparison
                answer.append(overlap)
                break
        else: # different
            answer.append(overlap)
            if idx == len(days) - 2: # last comparison
                answer.append(1)
                break
            else:
                overlap = 1

    return answer

# result = [2, 1] # 7 -> 2, 9 -> 1
# progresses = [93, 30, 55] # 7 / 3 -> 7 / 9
# speeds = [1, 30, 5]

# result = [1, 3, 2]
progresses = [95, 90, 99, 99, 80, 99] # 5 -> 1, 10 -> 3, 20 -> 2
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))
