# date: 2021.09.30
# author: jeiyoon
def solution(s: str) -> int:
  number_vocab = ["zero", 
                  "one", 
                  "two", 
                  "three",
                  "four",
                  "five",
                  "six",
                  "seven",
                  "eight",
                  "nine"]
  for number_int, number_str in enumerate(number_vocab):
    s = s.replace(number_str, str(number_int))
  return int(s)

s_list = ["one4seveneight", # 1478
     "23four5six7", # 234567
     "2three45sixseven", # 234567
     "123"] # 123

for s in s_list:
  print(solution(s))
