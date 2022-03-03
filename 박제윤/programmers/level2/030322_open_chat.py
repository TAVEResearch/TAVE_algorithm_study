# date: 2022.03.03 
# author: jeiyoon
from typing import List
from collections import defaultdict

def solution(record: List[str]) -> List[str]:
  system_record_list, result = [], []
  nickname_dict = defaultdict()

  """
  (1) Change nickname
  """
  for record_str in record:
    system_record_list.append(record_str.split())
    
    # Leave -> not append
    if len(system_record_list[-1]) == 2:
      continue
    
    _, uid, nickname = system_record_list[-1] 
    nickname_dict[uid] = nickname # change nickname (if key is not empty, overwrite it)

  """
  (2) print records
  """
  for system_record in system_record_list:
    if system_record[0] == 'Enter':
      result.append("{}님이 들어왔습니다.".format(nickname_dict[system_record[1]]))
    elif system_record[0] == "Leave":
      result.append("{}님이 나갔습니다.".format(nickname_dict[system_record[1]]))

  return result

# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))

# # date: 2021.08.13
# # author: jeiyoon
# from typing import List
# from collections import defaultdict

# def solution(record: List[str]) -> List[str]:
#     answer = []
#     nickname_log = defaultdict(str)

#     for idx, r in enumerate(record):
#       if len(r.split()) == 3: # Enter, Change
#         action = r.split()[0]
#         user_id = r.split()[1]
#         user_id_real = r.split()[2]

#       else: # Leave
#         action = r.split()[0]
#         user_id = r.split()[1]

#       if action == "Enter" or action == "Change": 
#         nickname_log[user_id] = user_id_real
#       else: # action == "Leave":
#         pass
    
#     for r in record:
#       action = r.split()[0]
#       if action == "Enter":
#         answer.append("{}님이 들어왔습니다.".format(nickname_log[r.split()[1]]))
#       elif action == "Leave":
#         answer.append("{}님이 나갔습니다.".format(nickname_log[r.split()[1]]))
#       else: # change
#         pass

#     return answer
