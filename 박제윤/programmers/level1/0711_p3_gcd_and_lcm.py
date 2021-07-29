from typing import List

def solution(n: int, m: int) -> List[int]:
    answer, n_divisor, m_divisor, divisor = [], [], [], []
    multiple = 1

    # divisor of n    
    for _n in range(1, n+1):
      if n % _n == 0:
        n_divisor.append(_n)

    # divisor of m
    for _m in range(1, m+1):
      if m % _m == 0:
        m_divisor.append(_m)

    # The greatest common denominator (GCD)
    for i in n_divisor:
      if i in m_divisor:
        divisor.append(i)
      else:
        pass

    answer.append(max(divisor))

    # The least common multiple (LCM)
    multiple = answer[0] * (n / answer[0]) * (m / answer[0])
    
    answer.append(int(multiple))
    
    return answer

n = 3
m = 12

# n = 2
# m = 5

solution(n, m)
