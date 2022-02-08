
def solution(n):
    answer = 2
    while n % answer != 1:
        answer += 1
    return answer
  
  
