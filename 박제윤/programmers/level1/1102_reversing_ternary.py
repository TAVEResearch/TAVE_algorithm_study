# date: 2021.11.02
# author: jeiyoon
def solution(n):
  answer = 0
  n_ternary = []
  
  # (1) n을 3진법 상에서 앞뒤로 뒤집은 후,
  while n >= 3:
    n_ternary.append(n % 3)
    n = (n // 3)
  n_ternary.append(n)    
  
  # (2) 이를 다시 10진법으로 표현한 수
  for idx, coef in enumerate(n_ternary):
    answer += coef * 3 ** (len(n_ternary) -1 - idx)

  return answer

# result = 7
# n = 45

# result = 229
n = 125
# n = 3
print(solution(n))
