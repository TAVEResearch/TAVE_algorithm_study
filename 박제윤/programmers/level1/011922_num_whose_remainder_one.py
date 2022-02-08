# date: 2022.01.19
# author: jeiyoon
def solution(n: int) -> int:
    return [x for x in range(1, n+1) if n % x == 1][0]

# result = 3
n = 10

# result =11
# n = 12

print(solution(n))
