# date: 2022.01.21
# author: jeiyoon
from typing import List
# from collections import defaultdict: 키 중복이 안됨
from collections import Counter

def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
  answer: list = []
  report_table: list = []
  report_count: list = []

  # 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
  report = list(set(report))
  
  """
  1. 유저 ID 
  """
  for id in id_list:
    report_table.append([id, [], []])

  """
  2. 유저가 신고한 ID 
  """
  for r in report:
    user_id = r.split()[0]
    reported_id = r.split()[1]
    report_count.append(r.split()[1])
    report_table[id_list.index(user_id)][1].append(reported_id)

  report_count = Counter(report_count) 
  """
  3. 정지된 ID
  """
  for r in report_table:
    for reported_r in r[1]:
      if report_count[reported_r] >= k:
        r[2].append(reported_r)
  
  for ban_count in report_table:
    answer.append(len(ban_count[2]))
  return answer


# result = [2,1,1,0]
# id_list = ["muzi", # 0
#            "frodo", # 1 
#            "apeach", # 2 
#            "neo", # 3
#            ] 

# report = ["muzi frodo",
#           "apeach frodo",
#           "frodo neo",
#           "muzi neo",
#           "apeach muzi"]

# k = 2

# result = [0,0]
id_list = ["con", 
           "ryan"]
report = ["ryan con", 
          "ryan con", 
          "ryan con", 
          "ryan con"]
k = 3

print(solution(id_list, report, k))
