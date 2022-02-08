# date: 2022.01.21
# author: jeiyoon
from typing import List

# True -> 1 (1, 1), False -> (0, -1)
# therefore, y = 2x - 1
def solution(absolutes: List[int], signs: List[bool]) -> int:
    return sum([(2 * int(sign) - 1) * absolute for absolute, sign in zip(absolutes, signs)])

# result = 9
absolutes = [4,7,12]	
signs = [True, False, True]	

# result = 0
# absolutes = [1,2,3]
# signs = [False, False, True]

print(solution(absolutes, signs))
