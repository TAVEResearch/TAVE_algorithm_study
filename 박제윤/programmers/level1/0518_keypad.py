# date: 2021.05.18
# author: jeiyoon

from typing import List

# def dist(p1, p2):
#     x = p2[0] - p1[0]
#     y = p2[1] - p1[1]
#
#     return math.sqrt(x*x + y*y)

def dist(p1: List[int], p2: List[int]) -> int:
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]

    return abs(x) + abs(y)

def solution(numbers: List[int], hand: str) -> str:
    l_list = [1, 4, 7]
    r_list = [3, 6, 9]
    coordinate_dict = {1: [1, 4],
                       2: [2, 4],
                       3: [3, 4],
                       4: [1, 3],
                       5: [2, 3],
                       6: [3, 3],
                       7: [1, 2],
                       8: [2, 2],
                       9: [3, 2],
                       "*": [1, 1],
                       0: [2, 1],
                       "#": [3, 1]}

    l_pos, r_pos = "*", "#"
    answer = ''

    for n in numbers:
        if n in l_list: # [1 4 7]
            answer += "L"
            l_pos = n 
        elif n in r_list: # [3 6 9]
            answer += "R"
            r_pos = n 
        else: # [2 5 8 0]
            if dist(coordinate_dict[l_pos], coordinate_dict[n]) \
                    < dist(coordinate_dict[r_pos], coordinate_dict[n]):
                answer += "L"
                l_pos = n
            elif dist(coordinate_dict[l_pos], coordinate_dict[n]) \
                    > dist(coordinate_dict[r_pos], coordinate_dict[n]):
                answer += "R"
                r_pos = n
            else:
                if hand == "left":
                    answer += "L"
                    l_pos = n
                else:
                    answer += "R"
                    r_pos = n

    return answer
