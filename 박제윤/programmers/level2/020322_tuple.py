# date: 2022.02.03
# author: jeiyoon
from typing import List
import re

def solution(s: str) -> List[int]:
  result = []
  """
  (1) extract num list from s
  """
  extracted_num_list = re.findall('\{([^)]+)\}', s)
  deduplication_list = []

  """
  (2) parsing
  """
  for extracted_num in extracted_num_list[0].split('},{'):
    extracted_num = extracted_num.replace('{', '')
    extracted_num = extracted_num.replace('}', '')
    extracted_num = extracted_num.split(',')
    deduplication_list.append(extracted_num)

  """
  (3) deduplication & preserve the order
  """
  for dedu_nums in sorted(deduplication_list, key = lambda x: len(x)):
    for num in dedu_nums:
      if int(num) not in result:
        result.append(int(num))
   
  return result

s_list = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", # [2, 1, 3, 4]
          "{{1,2,3},{2,1},{1,2,4,3},{2}}", # [2, 1, 3, 4]
          "{{20,111},{111}}", # [111, 20]
          "{{123}}", # [123]
          "{{4,2,3},{3},{2,3,4,1},{2,3}}", # [3, 2, 4, 1]
          ] 

for s in s_list:
  print(solution(s))
