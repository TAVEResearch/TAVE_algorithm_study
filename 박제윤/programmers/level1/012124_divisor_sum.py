# date: 2022.01.24
# author: jeiyoon
def solution(n: int) -> int:
  return sum([num for num in range(1, n + 1) if n % num == 0])

# return = 28
# n = 12 # 1 2 3 4 6 12

# return = 6
n = 5 # 1 5

print(solution(n))
