# date: 2021.10.13
# author: jeiyoon
# 교휸: Counter 사용법 
# https://ek-koh.github.io/python/counter/
from typing import List
import re
from collections import Counter

def jaccard_similarity(str1_list: List[str], str2_list: List[str]) -> float:
  # (5) only alphabet
  str1_list = [str1 for str1 in str1_list if str1.isalpha()]
  str2_list = [str2 for str2 in str2_list if str2.isalpha()]

  if len(str1_list) == 0 and len(str2_list) == 0:
    return 1
  
  # (6) intersection & sum of sets
  A_n_B = (Counter(str1_list) & Counter(str2_list)).values()
  A_U_B = (Counter(str1_list) | Counter(str2_list)).values()

  return sum(list(A_n_B)) / sum(list(A_U_B))

def solution(str1: str, str2: str) -> int:
    # (1) check the empty set
    if len(str1) == 0 and len(str2) == 0:
      return 1 * 65536
    
    # (2) lower case & only alphabet
    # 여기서 온리 알파벳 ㄴㄴ 
    str1 = str1.lower()
    str2 = str2.lower()

    # (3) splits two of each into list
    str1_list, str2_list = [], []
    for idx in range(len(str1) - 1):
      str1_list.append(str1[idx:idx+2])

    for idx in range(len(str2) - 1):
      str2_list.append(str2[idx:idx+2])

    # (4) jaccard similarity
    return int(jaccard_similarity(str1_list, str2_list) * 65536)

str1_list = ["FRANCE", # 16384
             "handshake",# 65536 
             "aa1+aa2", # 43690
             "E=M*C^2"] # 65536

str2_list = ["french",
             "shake hands",
             "AAAA12",
             "e=m*c^2"]

for str1, str2 in zip(str1_list, str2_list):
  print(solution(str1, str2))
