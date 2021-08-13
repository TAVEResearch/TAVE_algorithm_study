# date: 2021.08.13
# author: jeiyoon
from typing import List
from collections import defaultdict

def solution(record: List[str]) -> List[str]:
    answer = []
    nickname_log = defaultdict(str)

    for idx, r in enumerate(record):
      if len(r.split()) == 3: # Enter, Change
        action = r.split()[0]
        user_id = r.split()[1]
        user_id_real = r.split()[2]

      else: # Leave
        action = r.split()[0]
        user_id = r.split()[1]

      if action == "Enter" or action == "Change": 
        nickname_log[user_id] = user_id_real
      else: # action == "Leave":
        pass
    
    for r in record:
      action = r.split()[0]
      if action == "Enter":
        answer.append("{}님이 들어왔습니다.".format(nickname_log[r.split()[1]]))
      elif action == "Leave":
        answer.append("{}님이 나갔습니다.".format(nickname_log[r.split()[1]]))
      else: # change
        pass

    return answer
