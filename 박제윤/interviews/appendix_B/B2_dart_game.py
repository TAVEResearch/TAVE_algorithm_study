# date: 2021.10.06
# author: jeiyoon
import re 

def solution(dartResult: str) -> int:
    answer = 0
    list_for_split = []

    # 3S or 10S or 3S* or 10S*
    # sm ssm smt ssmt 
    # m 아니면 t로 끝남
    # 즉, 문자 숫자 or 특수문자 숫자 패턴만 끊으면 됨
    # ms -> m s / ts -> t s 
    # e.g.) 1D2S#10S -> sm smt ssm -> 1D 2S# 10S 
    for idx in range(len(dartResult) - 1):
      list_for_split.append(dartResult[idx])
      
      # charnum -> char num
      pattern_1_char = bool(re.compile('[A-Z]').match(dartResult[idx])) # char
      pattern_1_num = bool(re.compile('[0-9]').match(dartResult[idx + 1])) # num   
      
      if pattern_1_char and pattern_1_num:
        list_for_split.append(' ')
             
      # specialnum -> special num
      pattern_2_special = bool(re.compile('[*#]').match(dartResult[idx]))
      pattern_2_num = bool(re.compile('[0-9]').match(dartResult[idx + 1]))

      if pattern_2_special and pattern_2_num:
        list_for_split.append(' ')
    
    list_for_split.append(dartResult[-1])
    dart_result_list = ("".join(list_for_split)).split(" ") 

    score_list = [1, ] * 3
    power_dict = {"S":1, "D":2, "T":3}

    for idx, each_shot in enumerate(reversed(dart_result_list)):
      if "10" in each_shot: # got 10 point
        score = int(each_shot[0] + each_shot[1]) ** power_dict[each_shot[2]]    
      else: # no hit on 10
        score = int(each_shot[0]) ** power_dict[each_shot[1]]
      
      # minus
      if "#" in each_shot:
        score_list[2 - idx] *= -1
      # bonus
      elif "*" in each_shot:
        if idx == 2: # first_term
          score_list[2 - idx] *= 2
        else: # not a first_term
          score_list[2 - idx] *= 2
          score_list[2 - idx - 1] *= 2
      else:
        pass
      score_list[2 - idx] *= score

    return sum(score_list)

dart_Result_list = ["1S2D*3T", # 37 -> (1^1 * 2) + (2^2 * 2) + (3^3)
                    "1D2S#10S", # 9
                    "1D2S0T", # 3
                    "1S*2T*3S", # 23
                    "1D#2S*3S", # 5
                    "1T2D3D#", # -4
                    "1D2S3T*"] # 59

for dart_result in dart_Result_list:
  print(dart_result)
  print(solution(dart_result))
