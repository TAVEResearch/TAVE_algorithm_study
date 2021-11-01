# date: 2021.11.01
# author: jeiyoon
"""
Mission

1) 주어진 정수를 이진수로 변환
2) 두 리스트의 or 연산
3) "#"와 " "로 변환된 하나의 리스트로 출력
"""
from typing import List

def secret_map(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
  # 1) 리스트 내 정수를 이진수로 변환
  arr1_binary_list = []
  arr2_binary_list = []
  secret_map = []

  for a1, a2 in zip(arr1, arr2):
    a1_padding = "0" * (n - len(bin(a1)[2:]))
    a2_padding = "0" * (n - len(bin(a2)[2:]))
    
    arr1_binary_list.append(a1_padding + bin(a1)[2:])
    arr2_binary_list.append(a2_padding + bin(a2)[2:])
    
  # 2) 두 리스트의 "OR" 연산
  # print(arr1_binary_list)
  # print(arr2_binary_list)
  
  for a1_b, a2_b in zip(arr1_binary_list, arr2_binary_list):
    map_each_row = ""
    for a1_b_char, a2_b_char in zip(a1_b, a2_b):
      # print(int(a1_b_char) | int(a2_b_char))
      if int(a1_b_char) | int(a2_b_char):
        map_each_row += "#"
      else:
        map_each_row += " "
    # 3) "#"와 " "로 변환된 하나의 리스트로 출력
    # print(map_each_row)
    secret_map.append(map_each_row)
    
  return secret_map
  
# result = ["#####", 
#           "# # #", 
#           "### #",
#           "# ## ",
#           "#####"]
# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]

# result = ["######",
#           "###  #",
#           "##  ##",
#           "####  ",
#           "### # "]
n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

print(secret_map(n, arr1, arr2))
