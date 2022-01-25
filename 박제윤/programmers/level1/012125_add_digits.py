# date: 2022.01.25
# author: jeiyoon
def solution(N: int) -> int:
  return sum([int(n) for n in str(N)])

# answer = 6
# N = 123

# answer = 24
N = 987

print(solution(N))
