# date: 2022.01.25
# author: jeiyoon
from math import sqrt

def solution(n:int) -> int:
  x = sqrt(n)

  if n == int(pow(int(x), 2)):
    return int(pow(int(x) + 1, 2))
  else:
    return -1
  

# return = 144
n = 121

# return = -1
# n = 3

print(solution(n))
