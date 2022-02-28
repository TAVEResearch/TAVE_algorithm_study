# date: 2022.02.22
# author: jeiyoon
def solution(n: int) -> int:
  result = []
  world_list = ["4", "1", "2"]

  while n > 3: # n은 500,000,000이하의 자연수 입니다.
    result.append(world_list[n % 3]) 
    n = (n // 3) -1 * (int(n % 3 == 0))

  result += world_list[n % 3]
  result.reverse()

  return "".join(result)

for n in range(1, 14):
  print(solution(n))
  print(" ")



# """
# Timeout error occurs and i dont know why
# """
# from itertools import product

# def solution(n: int) -> int:
#   # 500,000,000
#   for p in range(19): # power is 0 to 18  
#     if n - (3 ** p) >= 0: 
#       n = n - (3 ** p)
#     else:
#       return "".join(list(product(['1', '2', '4'], repeat = p))[n])
    
# n_list = [i for i in range(1,14)]
# print(n_list)
# for n in n_list:
#   # print("n: ", n)
#   print(solution(n))
