# date: 2022.02.04
# author: jeiyoon
import sys
from typing import List
from collections import Counter
from itertools import combinations

def solution(orders: List[str], course: List[int]) -> List[str]:
  answer = []
  course_menu = Counter()
  max_count = -sys.maxsize

  for course_size in course:
    for order in orders:
      course_menu += Counter(combinations(sorted(order), course_size))

    for menu, count in course_menu.most_common():
      """
      (1) max count
      """
      if count >= max_count and count != 1:
        max_count = count
      
      """
      (2) check duplication
      """
      if count == max_count:
        answer.append(''.join(menu))
    
    """
    (3) reinit
    """
    course_menu = Counter([])
    max_count = -sys.maxsize
  
  return sorted(answer)

# 각 손님들이 주문한 단품메뉴
orders_list = [["ABCFG", 
                "AC", 
                "CDE", 
                "ACDE", 
                "BCFG", 
                "ACDEH"], # ["AC", "ACDE", "BCFG", "CDE"]
               ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], # ["ACD", "AD", "ADE", "CD", "XYZ"]
               ["XYZ", "XWY", "WXA"], # ["WX", "XY"]
               ]

# 코스요리를 구성하는 담품메뉴들의 개수
course_list = [[2,3,4],
               [2,3,5],
               [2,3,4],
               ]

# 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로
# 사전 순으로 오름차순 정렬해서
for orders, course in zip(orders_list, course_list):
  print(solution(orders, course))
  print(" ")
