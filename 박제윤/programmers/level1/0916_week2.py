# date: 2021.09.16
# author: jeiyoon
from typing import List

def grade(mean_score: int) -> str:
  if mean_score >= 90:
    return "A"
  elif mean_score >= 80 and mean_score < 90:
    return "B"
  elif mean_score >= 70 and mean_score < 80:
    return "C"
  elif mean_score >= 50 and mean_score < 70:
    return "D"
  else: # 50 and under
    return "F"
    
def solution(scores: List[List[int]]) -> str:
    answer = ''
    scores_transpose = [ [] for _ in range(len(scores[0]))] # slots
    
    # transpose the list for easy calculation
    for score in scores:
      for idx in range(len(score)):
        scores_transpose[idx].append(score[idx])

    for student_id, score_t in enumerate(scores_transpose):
      # the student got max score or min score
      if student_id == score_t.index(max(score_t)) or student_id == score_t.index(min(score_t)):
        # it's unique
        if score_t.count(score_t[student_id]) == 1:
          score_t.pop(student_id)

      answer += (grade(sum(score_t) / len(score_t)))
    
    return answer

# result = "FBABD"
scores = [[100,90,98,88,65],
          [50,45,99,85,77],
          [47,88,95,80,67],
          [61,57,100,80,65],
          [24,90,94,75,65]]

# result = "DA"
# scores = [[50,90],
#           [50,87]]

# scores = [[],
#           []]

# result = "CFD"
# scores = [[70,49,90],
#           [68,50,38],
#           [73,31,100]]

print(solution(scores))
