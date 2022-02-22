# date: 2022.02.22
# author: jeiyoon
"""
바보짓: for문에 max_print_size넣었음
이렇게 하면 100번 넘게 도는 연산은 그냥 안돌아서 틀렸다고 나옴
"""
from typing import List
from collections import deque

def solution(priorities: List[int], location: int) -> int:
  """
  (1) bi-directional push and pop are needed -> deque
  """
  answer = 0
  max_print_size = 100 # 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
  priorities = deque(priorities)
  init_priorities_size = len(priorities)

  for _ in range(max_print_size * max_print_size):
    """
    (2) the max value?
    """
    if priorities[0] == max(priorities):
      """
      (3) my document?  
      """
      if location == 0:
        priorities.popleft()
        answer = init_priorities_size - len(priorities) 
        break

      priorities.popleft()
    # not the max value
    else:
      priorities.append(priorities.popleft())

    # underflow
    if location == 0:
      location = len(priorities) - 1  
    else:
      location -= 1

  return answer

# return = 1
# priorities = [2, 1, 3, 2]
# location = 2

# return = 5
priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
