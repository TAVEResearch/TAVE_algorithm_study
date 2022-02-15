"""
양의 정수 n에 대해 n이 양의 정수 x의 제곱인지 아닌지 판단 
n의 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴
n이 양의 정수 x의 제곱이 아니라면 -1을 리턴 
"""

import math


def solution(n):
    nSqrt = math.sqrt(n)
    print(nSqrt)
    if n == math.pow(int(nSqrt), 2):
        return int(math.pow(nSqrt + 1, 2))
    else:
        return -1


# ----------- 다른 사람 풀이 ------------------
def nextSqure(n):
    sqrt = n ** (1 / 2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return "no"


print(solution(121))
