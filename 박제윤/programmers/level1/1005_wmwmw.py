# date: 2021.10.05
# author: jeiyoon
def solution(n: int) -> str:
    return "수박" * (n // 2)  + "수" * (n % 2)
  
  
  
# result = "수박수"
n = 3

# result = "수박수박"
# n = 4

print(solution(n))
