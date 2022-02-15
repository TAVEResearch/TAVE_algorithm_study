def solution(n):
    n = n ** (1/2)
    if n.is_integer():
        answer = (n + 1) ** 2
    else:
        answer = -1
    return answer
    