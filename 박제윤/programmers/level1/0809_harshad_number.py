# date: 2021.08.09
# author: jeiyoon
def solution(x: int) -> bool:
  return not (x % sum(list(map(int, str(x)))))
