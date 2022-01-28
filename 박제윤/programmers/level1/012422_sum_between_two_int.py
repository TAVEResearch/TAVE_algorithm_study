# date: 2022.01.24
# author: jeiyoon
def solution(a: int, b: int) -> int:
  return sum([num for num in range(min(a, b), max(a, b) + 1)])

# return = 12
# a = 3
# b = 5

# return = 3
# a = 3
# b = 3

# return = 12
a = 5
b = 3

print(solution(a, b))
