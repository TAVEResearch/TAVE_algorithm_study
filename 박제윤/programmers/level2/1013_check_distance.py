# date: 2021.10.13
# author: jeiyoon
# 교훈: break와 continue를 사용할때 조심할것
from typing import List

def manhattan_distance(p1: List[int], p2: List[int]) -> int:
  return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def solution(places: List[List[str]]) -> List[int]:
    answer = []

    for place in places:
      coordinates_of_p = []
      # 1) p의 좌표 모두 구하기
      for idx_row, seats in enumerate(place):
        for idx_col, seat in enumerate(seats):
          if seat == "P":
            coordinates_of_p.append([idx_row, idx_col])
      if len(coordinates_of_p) == 0:
        answer.append(1)
        continue # break?: 다 안돌았는데 places에 걸린 loop가 나가져서 안됨

      # 2) p좌표 끼리 맨해튼 거리 계산
      partition_check_list = []
      for p1 in range(len(coordinates_of_p) - 1):
        for p2 in range(p1 + 1, len(coordinates_of_p)):
          dist = manhattan_distance(coordinates_of_p[p1], coordinates_of_p[p2])
          if dist <=2:
            partition_check_list.append([coordinates_of_p[p1], coordinates_of_p[p2]])

      # 3) 맨해튼 거리가 모두 3 이상이면 통과
      if len(partition_check_list) == 0:
        answer.append(1)
        continue # 여기가 절대로 break가 되면 안됨

      # 4) 맨해튼 거리가 2 이하인게 있으면 가림막 조사
      true_flag_list = []

      for partition_check in partition_check_list:
        p1_x = partition_check[0][0]
        p1_y = partition_check[0][1]
        p2_x = partition_check[1][0]
        p2_y = partition_check[1][1] 

        # 5) 가림막 잘 되어있으면 통과
        # 5-1) P X P
        # horizontal
        # 가로로 되어있는게 PXP 일수도 있고 PP 일수도 있음
        if p1_x == p2_x and p1_y != p2_y:
          if abs(p1_y - p2_y) == 1: # PP
            answer.append(0)
            break 
          # P X P  
          x = p1_x
          y = int((p1_y + p2_y) / 2)

          if place[x][y] != "X": # P or O
            answer.append(0)
            break
          else:
            true_flag_list.append(1)
            continue

        # vertical
        elif p1_y == p2_y and p1_x != p2_x:
          if abs(p1_x - p2_x) == 1: # PP
            answer.append(0)
            break 
          x = int((p1_x + p2_x) / 2)
          y = p1_y

          if place[x][y] != "X": # P or O
            answer.append(0)
            break
          else:
            true_flag_list.append(1)
            continue

        # diagonal
        elif p1_x != p2_x and p1_y != p2_y: # 두 p가 x,y 모두 다름
          # 5-2) P X X P (2, 2)
          if place[p1_x][p2_y] != "X" or place[p2_x][p1_y] != "X":
            answer.append(0)
            break
          else:
            true_flag_list.append(1)
            continue
        else:
          pass

      if len(true_flag_list) == len(partition_check_list):
        answer.append(1)

    return answer

# result = [1, 0, 1, 1, 1]
places =[["POOOP", 
          "OXXOX", 
          "OPXPX", 
          "OOXOX", 
          "POXXP"], 
         ["POOPX", 
          "OXPXP", 
          "PXXXO", 
          "OXXXO", 
          "OOOPP"], 
         ["PXOPX", 
          "OXOXP", 
          "OXPOX", 
          "OXXOP", 
          "PXPOX"], 
         ["OOOXX", 
          "XOOOX", 
          "OOOXX", 
          "OXOOX", 
          "OOOOO"], 
         ["PXPXP",# 3 4 2 4 3 3 4 2 3 2 1 1 0  
          "XPXPX", 
          "PXPXP", 
          "XPXPX", 
          "PXPXP"], # added case
         ["XXXXX",
          "PPPXX",
          "XXXXX",
          "XXXXX",
          "XXXXX"]
         ]

print("result: ", solution(places))
