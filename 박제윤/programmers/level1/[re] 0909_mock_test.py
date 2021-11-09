# date: 2021.09.09
# author: jeiyoon
# 너무 못풀어서 자괴감옴 다시 풀어볼것
from typing import List

def solution(answers: List[int]) -> List[int]:
  i_hate_math_1_list = [1, 2, 3, 4, 5] * 2000 # 5
  i_hate_math_2_list = [2, 1, 2, 3, 2, 4, 2, 5] * 1250 # 8
  i_hate_math_3_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000# 10
  
  i_hate_math_1_score, i_hate_math_2_score, i_hate_math_3_score = 0, 0, 0 
  
  for idx, a in enumerate(answers):
    if a == i_hate_math_1_list[idx]:
      i_hate_math_1_score += 1
    if a == i_hate_math_2_list[idx]:
      i_hate_math_2_score += 1    
    if a == i_hate_math_3_list[idx]:
      i_hate_math_3_score += 1
  
  max_count = max(i_hate_math_1_score, i_hate_math_2_score, i_hate_math_3_score)
  result = []

  if max_count == i_hate_math_1_score:
    result.append(1)
  if max_count == i_hate_math_2_score:
    result.append(2)  
  if max_count == i_hate_math_3_score:
    result.append(3)

  return result

result = [1]
answers = [1,2,3,4,5]

# result = [1,2,3]
# answer = [1,3,2,4,2]

print(solution(answers))
