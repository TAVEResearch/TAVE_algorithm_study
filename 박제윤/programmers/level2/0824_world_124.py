# date: 2021.08.24
# author: jeiyoon
"""
Timeout error occurs and i dont know why
"""
from itertools import product

def solution(n: int) -> int:
  # 500,000,000
  for p in range(19): # power is 0 to 18  
    if n - (3 ** p) >= 0: 
      n = n - (3 ** p)
    else:
      return "".join(list(product(['1', '2', '4'], repeat = p))[n])
    
n_list = [i for i in range(1,14)]
print(n_list)
for n in n_list:
  # print("n: ", n)
  print(solution(n))
