# date: 2021.09.16
# author: jeiyoon
from typing import List
import sys

def solution(table: List[str], languages: List[str], preference: List[int]) -> str:
    answer = ''
    max_score = -sys.maxsize # min

    # each job
    for t in table:
      t_list = t.split()
      total_score = 0
      for l, p in zip(languages, preference):
        try:
          idx = t_list.index(l)
        except ValueError:
          idx = 6
        
        score = 5 - (idx - 1)
        total_score += score * p
      
      if total_score > max_score:
        max_score = total_score
        answer = t_list[0]
      
      # equals -> lexical order
      elif total_score == max_score:
        if not answer > t_list[0]:# ascending order: answer -> t_list[0] 
          pass
        else: # t_list[0] -> answer  
          answer = t_list[0]
      
      else:
        pass
    
    return answer

# result = "HARDWARE"
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", 
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
         "GAME C++ C# JAVASCRIPT C JAVA"]

languages = ["PYTHON", "C++", "SQL"]

preference = [7, 5, 5]


# # result = "PORTAL"
# table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", 
#          "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
#          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
#          "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
#          "GAME C++ C# JAVASCRIPT C JAVA"]

# languages = ["JAVA", "JAVASCRIPT"]
# preference = [7, 5]

print(solution(table, languages, preference))
