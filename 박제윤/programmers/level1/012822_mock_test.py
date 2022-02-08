# date: 2022.01.28
# author: jeiyoon
from typing import List

def solution(answers: List[int]) -> List[int]:
  supo_one: list = [1, 2, 3, 4, 5]
  supo_two: list = [2, 1, 2, 3, 2, 4, 2, 5]
  supo_three: list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

  supo_score_list = [0] * 3  

  # count correct answers
  for idx, answer in enumerate(answers):
    if answer == supo_one[idx % len(supo_one)]:
      supo_score_list[0] += 1      
    if answer == supo_two[idx % len(supo_two)]:
      supo_score_list[1] += 1      
    if answer == supo_three[idx % len(supo_three)]:
      supo_score_list[2] += 1      

  return [idx + 1 for idx, score in enumerate(supo_score_list) if score >= max(supo_score_list)]


# return = [1]
# answers = [1,2,3,4,5]

# return = [1,2,3]
answers = [1,3,2,4,2]	

print(solution(answers))
