# date: 2021.08.13
# author: jeiyoon
def solution(W: int, H: int) -> int:
  # exception
  if W == H: # square
    return W * (H - 1)

  # exception
  if W == 1 or H == 1: # unit square
    return 0
    
  answer = 0

  # inclination
  inclination = -1 * float(H / W)
  
  for w in range(1, W):
    answer += int(inclination * w + H)  

  return answer * 2
