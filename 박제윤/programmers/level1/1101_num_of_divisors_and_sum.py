# date: 2021.11.01
# author: jeiyoon
from typing import List

def finding_divisors(number: int) -> int:
  div_list = []
  for candidate in range(1, number + 1):
    if number % candidate == 0:
      div_list.append(candidate)

  return div_list

def solution(left: int, right: int) -> int:
    answer = 0
    # 1. finding divisors
    for idx in range(left, right + 1):
      # 2. # of divisors
      if len(finding_divisors(idx)) % 2 == 0:
        answer += idx
      else:
        answer -= idx

    return answer


# result = 43
# left = 13
# right = 17

# result = 52
left = 24
right = 27

print(solution(left, right))
