# date: 2021.09.30
# author: jeiyoon
"""
통과는 했지만 마지막 reverse 조건 으로 짜면 안됨
프로그래머스에 문제가 없어짐...
"""
from typing import List

def solution(weights: List[int], head2head: List[str]) -> List[int]:
    boxer_list = []
    # win rate & win heavier
    for player, (weight, h) in enumerate(zip(weights, head2head)):
      # win rate
      # exception
      if h.count("N") == len(h):
        win_rate = 0
      else:
        win_rate = h.count("W") / (h.count("W") + h.count("L")) 
      
      # win heavier
      win_heavier = 0 
      for opponent, plyr_record in enumerate(h):
        if plyr_record == "W":
          if weights[player] < weights[opponent]:
            win_heavier += 1   
      boxer_list.append([win_rate, win_heavier, weight, player + 1])

    # priority: [win_rate, win_heavier, weight, smaller]
    boxer_list = sorted(boxer_list,  key = lambda x: (x[0], x[1], x[2]), reverse = True)

    return [p[-1] for p in boxer_list]
  
  
# result = [3,4,1,2]
# weights = [50,82,75,120]
# head2head = ["NLWL","WNLL","LWNW","WWLN"] #  33 33 66 66 

# # result = [2,3,1]
# weights = [145,92,86]
# head2head = ["NLW","WNL","LWN"]

# # result = [2,1,3]
weights = [60,70,60]
head2head = ["NNN","NNN","NNN"]

print(solution(weights, head2head))
