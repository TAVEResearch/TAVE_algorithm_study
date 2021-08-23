# date: 2021.08.23
# author: jeiyoon
def solution(s: str) -> int:
    min_length = len(s)

    for window_size in range(1, int(len(s)/2) + 1) : # the size of sliding window   
      coefficient = 1
      result = []
        
      for idx in range(0, len(s) - window_size, window_size):
        if s[idx:window_size + idx] == s[idx + window_size:window_size + idx + window_size]: # same
          coefficient += 1
        
          if idx >= len(s) - window_size - window_size: # last iteration
            result.append(str(coefficient) + s[idx:window_size + idx])
            
        else: # different
          if coefficient == 1:
            result.append(s[idx:window_size + idx])
          else:
            result.append(str(coefficient) + s[idx:window_size + idx])

          if idx >= len(s) - window_size - window_size: # last iteration
            result.append(s[idx + window_size:])
          
          coefficient = 1 # reset

      if min_length >= len("".join(result)):
        min_length = len("".join(result))

    return min_length

test_case = [
    "aabbaccc", # 7
    "ababcdcdababcdcd", # 9
    "abcabcdede", # 8
    "abcabcabcabcdededededede", # 14
    "xababcdcdababcdcd" # 17
]

for s in test_case:
  print(solution(s))
