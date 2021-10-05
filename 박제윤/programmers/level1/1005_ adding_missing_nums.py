# date: 2021.10.05
# author: jeiyoon
from typing import List

def solution(numbers: List[int]) -> int:
    return sum([n for n in list(range(10)) if n not in numbers])

  
# result = 14
# numbers = [1,2,3,4,6,7,8,0]

# result = 6
numbers = [5,8,4,0,6,7,9]

print(solution(numbers))
