# date: 2021.08.09
# author: jeiyoon
def solution(x: int) -> bool:
  sum = 0
  for digit in str(x):
    sum += int(digit)
    
  return not (x % sum)
