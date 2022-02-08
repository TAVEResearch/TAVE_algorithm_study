# date: 2022.01.20
# author: jeiyoon
from typing import List

def solution(sizes: List[List[int]]) -> int:
    width, height = [], []
    for size in sizes:
      width.append(max(size))
      height.append(min(size))

    return max(width) * max(height)


# result = 4000
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

# result = 120
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

# result = 133
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes))
